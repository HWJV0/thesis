"""Reflexion Agent strategies for Math."""

import re

from typing import Any, Dict, List, Optional, Tuple

import tiktoken

from langchain_core.language_models.chat_models import BaseChatModel
from tiktoken.core import Encoding

from agents.core.reflection.functional import (
    _prompt_cot_agent
)
from agents.core.reflection.reflect import (
    ReflexionCoTReflector
)
from agents.core.reflection.strategies.base import (
    ReflexionCoTBaseStrategy
)
from agents.eval.qa import qa_is_correct
from agents.utils.general import safe_execute
from agents.utils.parse import remove_newline


def parse_math_action_cot(action: str) -> Tuple[str, str]:
    """Parses an action string to extract the action type and code content.

    Identifies action types (`Finish`) and extracts the
    corresponding code content enclosed within Markdown-style code blocks.
    The action type is case-insensitive and the code content is trimmed of
    leading and trailing whitespace.

    Args:
        action (str): The action string containing the action type and code content.

    Returns:
        Tuple[str, str]: A tuple containing the extracted action type (capitalized)
        and the extracted code content.
    """
    action_split = action.split("```python", maxsplit=1)
    match = re.search(r"\b(Finish)\b", action_split[0], re.IGNORECASE)

    action_type = match.group(0).lower().capitalize() if match else ""
    try:
        query = action_split[1].split("```")[0].strip() if action_type else ""
    except:
        action_type = ""
        query = ""

    return action_type, query


def parse_math_action_react(action: str) -> Tuple[str, str]:
    """Parses an action string to extract the action type and code content.

    Identifies action types (`Finish`, `Calculate`) and extracts the
    corresponding code content enclosed within Markdown-style code blocks.
    The action type is case-insensitive and the code content is trimmed of
    leading and trailing whitespace.

    Args:
        action (str): The action string containing the action type and code content.

    Returns:
        Tuple[str, str]: A tuple containing the extracted action type (capitalized)
        and the extracted code content.
    """
    action_split = action.split("```python", maxsplit=1)
    match = re.search(r"\b(Finish|Calculate)\b", action_split[0], re.IGNORECASE)

    action_type = match.group(0).lower().capitalize() if match else ""
    try:
        query = action_split[1].split("```")[0].strip() if action_type else ""
    except:
        action_type = ""
        query = ""

    return action_type, query


class ReflexionCoTMathStrategy(ReflexionCoTBaseStrategy):
    """A strategy class for Math benchmarks using the ReflexionCoT agent.

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
        thought = remove_newline(thought).split("Action")[0].strip()
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
        action = action.split("Observation")[0].strip()

        action_type, query = parse_math_action_cot(action)
        self._scratchpad += f" {action_type}[\n```python\n{query}\n```\n]"

        return action_type, query

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
        answer, _ = safe_execute(query)

        self._scratchpad += f"\nObservation: "
        if action_type.lower() == "finish":
            self._finished = True
            self._answer = query
            if qa_is_correct(str(answer[0]), int(key)):
                obs = "Generated answer is CORRECT."
            else:
                obs = "Generated answer is INCORRECT."
        else:
            obs = "Invalid action type, please try again."
        self._scratchpad += obs

        return qa_is_correct(str(answer[0]), int(key)), obs

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
        answer, _ = safe_execute(self._answer)
        return qa_is_correct(str(answer[0]), int(key)) or idx >= max_trials

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
        answer, _ = safe_execute(self._answer)
        return (
            idx > 0
            and not qa_is_correct(str(answer[0]), int(key))
            and reflect_strategy is not None
        )

class SelfReflectionCoTMathStrategy(ReflexionCoTMathStrategy):
    """A strategy class for continuous generation without external correctness evaluation using the ReflexionCoT agent."""

    def generate_observation(
        self, action_type: str, query: str, key: str
    ) -> Tuple[Optional[bool], str]:
        """Generates an observation based on the action type and query.

        Args:
            action_type (str): The type of action to be performed.
            query (str): The query for the action.
            key (str): The key for the observation.

        Returns:
            Tuple[Optional[bool], str]: A boolean indicating correctness (None in this strategy) and the generated observation.
        """
        answer, _ = safe_execute(query)

        self._scratchpad += f"\nObservation: "
        if action_type.lower() == "finish":
            self._finished = True
            self._answer = query
            obs = f"Generated answer is {answer[0]}."
        else:
            obs = "Invalid action type, please try again."
        self._scratchpad += obs

        # Model evaluates correctness internally but does not expose it externally
        is_correct = qa_is_correct(str(answer[0]), int(key))

        return is_correct, obs

    def halting_condition(self, idx: int, key: str, **kwargs: Any) -> bool:
        """Determines whether the halting condition has been met.

        Args:
            idx (int): The current step index.
            key (str): The key for the observation.
            **kwargs (Any): Additional arguments.

        Returns:
            bool: False to ensure continuous generation.
        """
        max_trials = kwargs.get("max_trials", self.max_trials)
        return idx >= max_trials  # Halt based on the maximum number of trials


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

class ReflexionCoTPoTGSM8KStrategy(ReflexionCoTMathStrategy):
    """A strategy class for the GSM8K benchmark using the ReflexionCoT agent."""

    pass

class SelfReflectionCoTPoTGSM8KStrategy(SelfReflectionCoTMathStrategy):
    """A strategy class for the GSM8K benchmark using the SelfReflectionCoT agent."""

    pass
