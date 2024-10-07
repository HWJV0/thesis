"""Reflexion Agent strategies for MATH Dataset."""

import re

from typing import Any, Dict, List, Optional, Tuple

import tiktoken

from langchain_core.language_models.chat_models import BaseChatModel
from tiktoken.core import Encoding

from agents.core.reflection.functional import (
    _prompt_cot_agent
)
from agents.core.reflection.reflect import (
    ReflexionCoTReflector,
)
from agents.core.reflection.strategies.base import (
    ReflexionCoTBaseStrategy,
)
from agents.utils.parse import remove_newline

from agents.eval.math import math_is_correct, last_boxed_only_string

def parse_finish_action(string: str) -> Tuple[str, str]:
    """Parses a finish action string into an action type and its argument.

    This method is used in Reflexion.

    Args:
        string (str): The action string to be parsed.

    Returns:
        Tuple[str, str]: A tuple containing the action type and argument.
    """
    pattern = r"(.*)Finish\[(.*?)\]"
    match = re.search(pattern, string, re.DOTALL) 

    if match:
        action_type = "Finish"
        argument = match.group(2)
    else:
        action_type = ""
        argument = ""
    return action_type, argument


class ReflexionCoTMATHQAStrategy(ReflexionCoTBaseStrategy):
    """A strategy class for MATH benchmarks using the ReflexionCoT agent.

    Attributes:
        llm (BaseChatModel): The language model used for generating answers and critiques.
        reflector (Optional[ReflexionCoTReflector]): The reflector used for generating reflections. Defaults to None.
        max_reflections (int): The maximum number of reflections allowed. Defaults to 3.
        max_trials (int): The maximum number of trials allowed. Defaults to 1.
    """

    def __init__(
        self,
        llm: BaseChatModel,
        reflector: Optional[ReflexionCoTReflector] = None,
        max_reflections: int = 3,
        max_trials: int = 1,
    ) -> None:
        """Initialization."""
        super().__init__(llm)
        self.llm = llm
        self.max_reflections = max_reflections
        self.max_trials = max_trials

        if not reflector:
            reflector = ReflexionCoTReflector(llm=llm, max_reflections=max_reflections)
        self.reflector = reflector

        self._scratchpad = ""
        self._finished = False
        self._answer = ""

    def generate(
        self,
        question: str,
        examples: str,
        reflections: str,
        prompt: str,
        additional_keys: Dict[str, str],
        **kwargs: Any,
    ) -> str:
        """Generates a thought based on the question, examples, and prompt.

        Args:
            question (str): The question to be answered.
            examples (str): Examples to guide the generation process.
            reflections (str): Reflections to consider during generation.
            prompt (str): The prompt used for generating the thought.
            additional_keys (Dict[str, str]): Additional keys for the generation process.
            **kwargs (Any): Additional arguments.

        Returns:
            str: The generated thought.
        """
        self._scratchpad += "\nThought:"
        thought = _prompt_cot_agent(
            llm=self.llm,
            examples=examples,
            reflections=reflections,
            question=question,
            scratchpad=self._scratchpad,
            prompt=prompt,
            additional_keys=additional_keys,
        )

        if "Action" in thought:
            thought = thought.split("Action")[0].strip()
        elif "Finish" in thought:
            thought = thought.split("Finish")[0].strip()
        else:
            thought = thought.strip()

        self._scratchpad += " " + thought

        return thought

    def generate_action(
        self,
        question: str,
        examples: str,
        reflections: str,
        prompt: str,
        additional_keys: Dict[str, str],
        **kwargs: Any,
    ) -> Tuple[str, str]:
        """Generates an action based on the question, examples, and prompt.

        Args:
            question (str): The question to be answered.
            examples (str): Examples to guide the generation process.
            reflections (str): Reflections to consider during generation.
            prompt (str): The prompt used for generating the action.
            additional_keys (Dict[str, str]): Additional keys for the generation process.
            **kwargs (Any): Additional arguments.

        Returns:
            Tuple[str, str]: The generated action type and query.
        """
        self._scratchpad += "\nAction:"
        action = _prompt_cot_agent(
            llm=self.llm,
            examples=examples,
            reflections=reflections,
            question=question,
            scratchpad=self._scratchpad,
            prompt=prompt,
            additional_keys=additional_keys,
        )

        action = action.strip()

        action_type, query = parse_finish_action(action)
        self._scratchpad += f" {action_type}[{query}]"
        
        return action_type, query

    def generate_observation(
        self, action_type: str, query: str, key: str
    ) -> Tuple[bool, str]:
        """Generates an observation based on the action type and query.

        Args:
            action_type (str): The type of action to be performed.
            query (str): The query for the action.
            key (NPMeetingPlanningSolution): The key for the observation.

        Returns:
            Tuple[bool, str]: A boolean indicating correctness and the generated observation.
        """

        self._scratchpad += f"\nObservation: "
        if action_type.lower() == "finish":
            self._finished = True
            self._answer = query
            if math_is_correct(self._answer, key):
                obs = "Generated answer is CORRECT."
            else:
                obs = "Generated answer is INCORRECT."
        else:
            obs = "Invalid action type, please try again."
        self._scratchpad += obs

        return math_is_correct(self._answer, key), obs

    def create_output_dict(
        self,
        thought: str,
        action_type: str,
        obs: str,
        is_correct: bool,
        reflections: List[str],
    ) -> Dict[str, Any]:
        """Creates a dictionary of the output components.

        Args:
            thought (str): The generated thought.
            action_type (str): The type of action performed.
            obs (str): The generated observation.
            is_correct (bool): Whether the answer is correct.
            reflections (List[str]): The reflections.

        Returns:
            Dict[str, Any]: A dictionary containing the thought, action type, observation, answer, is_correct, and reflections.
        """
        return {
            "thought": thought,
            "action_type": action_type,
            "observation": obs,
            "answer": self._answer,
            "is_correct": is_correct,
            "reflections": reflections,
        }

    def halting_condition(self, idx: int, key: str, **kwargs: Any) -> bool:
        """Determines whether the halting condition has been met.

        Args:
            idx (int): The current step index.
            key (str): The key for the observation.
            **kwargs (Any): Additional arguments.

        Returns:
            bool: True if the halting condition is met, False otherwise.
        """
        max_trials = kwargs.get("max_trials", self.max_trials)
        return math_is_correct(self._answer, key) or idx >= max_trials

    def reset(self, **kwargs: Any) -> None:
        """Resets the internal state of the strategy.

        Resets the scratchpad and the finished flag.
        Resets only the scratchpad if specified with 'only_scratchpad'.

        Args:
            **kwargs (Any): Additional arguments.
        """
        only_scratchpad = kwargs.get("only_scratchpad", False)
        if only_scratchpad:
            self._scratchpad = ""
        else:
            self.reflector.reset()
            self._scratchpad = ""
            self._finished = False
            self._answer = ""

    def reflect(
        self,
        reflect_strategy: str,
        question: str,
        examples: str,
        prompt: str,
        additional_keys: Dict[str, str],
    ) -> Tuple[List[str], str]:
        """Reflects on a given question, context, examples, prompt, and additional keys using the specified reflection strategy.

        Args:
            reflect_strategy (str): The strategy to use for reflection.
            question (str): The question to be reflected upon.
            examples (str): Examples to guide the reflection process.
            prompt (str): The prompt or instruction to guide the reflection.
            additional_keys (Dict[str, str]): Additional keys for the reflection process.

        Returns:
            Tuple[List[str], str]: The reflections and the reflection string.
        """
        reflections, reflections_str = self.reflector.reflect(
            reflect_strategy=reflect_strategy,
            question=question,
            examples=examples,
            scratchpad=self._scratchpad,
            prompt=prompt,
            additional_keys=additional_keys,
        )
        return reflections, reflections_str

    def reflect_condition(
        self, idx: int, reflect_strategy: Optional[str], key: str
    ) -> bool:
        """Determines whether the reflection condition has been met.

        Args:
            idx (int): The current step.
            reflect_strategy (Optional[str]): The strategy to use for reflection.
            key (str): The key for the observation.

        Returns:
            bool: True if the reflection condition is met, False otherwise.
        """

        return (
            idx > 0
            and not math_is_correct(self._answer, key)
            and reflect_strategy is not None
        )

class SelfReflectionCoTMATHQAStrategy(ReflexionCoTMATHQAStrategy):
    """A strategy class for Meeting Planning benchmarks using the SelfReflectionCoT agent.

    Attributes:
        llm (BaseChatModel): The language model used for generating answers and critiques.
        reflector (Optional[ReflexionCoTReflector]): The reflector used for generating reflections. Defaults to None.
        max_reflections (int): The maximum number of reflections allowed. Defaults to 3.
        max_trials (int): The maximum number of trials allowed. Defaults to 1.
    """

    def generate_observation(
        self, action_type: str, query: str, key: str
    ) -> Tuple[bool, str]:
        """Generates an observation based on the action type and query.

        Args:
            action_type (str): The type of action to be performed.
            query (str): The query for the action.
            key (str): The key for the observation.

        Returns:
            Tuple[bool, str]: A boolean indicating correctness and the generated observation.
        """

        self._scratchpad += f"\nObservation: "
        if action_type.lower() == "finish":
            self._finished = True
            self._answer = query
            obs = f"Generated answer is {last_boxed_only_string(query)}."

        else:   
            obs = "Invalid action type, please try again."
        self._scratchpad += obs

        return math_is_correct(self._answer, key), obs

    def halting_condition(self, idx: int, key: str, **kwargs: Any) -> bool:
        """Determines whether the halting condition has been met.

        Args:
            idx (int): The current step index.
            key (str): The key for the observation.
            **kwargs (Any): Additional arguments.

        Returns:
            bool: True if the halting condition is met, False otherwise.
        """
        max_trials = kwargs.get("max_trials", self.max_trials)
        return idx >= max_trials

    def reflect_condition(
        self, idx: int, reflect_strategy: Optional[str], key: str
    ) -> bool:
        """Determines whether the reflection condition has been met.

        Args:
            idx (int): The current step.
            reflect_strategy (Optional[str]): The strategy to use for reflection.
            key (str): The key for the observation.

        Returns:
            bool: True if the reflection condition is met, False otherwise.
        """

        return (
            idx > 0
            and reflect_strategy is not None
        )

class ReflexionCoTMATHAlgebraStrategy(ReflexionCoTMATHQAStrategy):
    """A strategy class for the MATH Algebra benchmark using the ReflexionCoT agent."""

    pass

class SelfReflectionCoTMATHAlgebraStrategy(SelfReflectionCoTMATHQAStrategy):
    """A strategy class for the Natural Plan Meeting Planning benchmark using the SelfReflectionCoT agent."""

    pass

class ReflexionCoTMATHNumberTheoryStrategy(ReflexionCoTMATHQAStrategy):
    """A strategy class for the MATH Algebra benchmark using the ReflexionCoT agent."""

    pass

class SelfReflectionCoTMATHNumberTheoryStrategy(SelfReflectionCoTMATHQAStrategy):
    """A strategy class for the Natural Plan Meeting Planning benchmark using the SelfReflectionCoT agent."""

    pass
