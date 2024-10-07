"""Reflexion Agent.

Original Paper: https://arxiv.org/abs/2303.11366
Paper Repositories:
    - https://github.com/noahshinn/reflexion-draft
    - https://github.com/noahshinn/reflexion
"""

import re

from typing import Any, Dict, List, Optional, Tuple

from langchain_core.language_models.chat_models import BaseChatModel

from agents.base.agent import BaseAgent
from agents.core.constants import Benchmarks

from agents.core.reflection.output import (
    ReflexionCoTOutput
)

from agents.core.reflection.reflect import (
    ReflexionCoTReflector
)

from agents.core.reflection.strategies.qa import (
    ReflexionCoTGSM8KStrategy,
    SelfReflectionCoTGSM8KStrategy
)

from agents.core.reflection.strategies.math import (
    SelfReflectionCoTPoTGSM8KStrategy,
    ReflexionCoTPoTGSM8KStrategy
)

from agents.core.reflection.strategies.math_qa import (
    ReflexionCoTMATHAlgebraStrategy,
    SelfReflectionCoTMATHAlgebraStrategy,
    ReflexionCoTMATHNumberTheoryStrategy,
    SelfReflectionCoTMATHNumberTheoryStrategy
)

# from agents.core.reflection.strategies.qa import (
#     ReflexionCoTGSM8KStrategy,
#     SelfReflectionCoTGSM8KStrategy
# )

from agents.core.reflection.strategies.schedule import (
    ReflexionCoTNPCalendarSchedulingStrategy,
    SelfReflectionCoTNPCalendarSchedulingStrategy
)

from agents.core.reflection.strategies.meeting_plan import (
    ReflexionCoTNPMeetingPlanningStrategy,
    SelfReflectionCoTNPMeetingPlanningStrategy
)

from agents.core.reflection.strategies.trip_plan import (
    ReflexionCoTNPTripPlanningStrategy,
    SelfReflectionCoTNPTripPlanningStrategy
)

SELFREFLECTION_COT_STRATEGIES = {
    Benchmarks.GSM8K: SelfReflectionCoTGSM8KStrategy,
    Benchmarks.POTGSM8K: SelfReflectionCoTPoTGSM8KStrategy,

    Benchmarks.MATHALGEBRA: SelfReflectionCoTMATHAlgebraStrategy,
    Benchmarks.NUMBERTHEORY: SelfReflectionCoTMATHNumberTheoryStrategy,

    Benchmarks.NPCALLENDARSCHEDULING: SelfReflectionCoTNPCalendarSchedulingStrategy,
    Benchmarks.NPMEETINGPLANNING: SelfReflectionCoTNPMeetingPlanningStrategy,
    Benchmarks.NPTRIPPLANNING: SelfReflectionCoTNPTripPlanningStrategy
}

REFLEXION_COT_STRATEGIES = {
    Benchmarks.GSM8K: ReflexionCoTGSM8KStrategy,
    Benchmarks.POTGSM8K: ReflexionCoTPoTGSM8KStrategy,

    Benchmarks.MATHALGEBRA: ReflexionCoTMATHAlgebraStrategy,
    Benchmarks.NUMBERTHEORY: ReflexionCoTMATHNumberTheoryStrategy,

    Benchmarks.NPCALLENDARSCHEDULING: ReflexionCoTNPCalendarSchedulingStrategy,
    Benchmarks.NPMEETINGPLANNING: ReflexionCoTNPMeetingPlanningStrategy,
    Benchmarks.NPTRIPPLANNING: ReflexionCoTNPTripPlanningStrategy
}


def parse_action(string: str) -> Tuple[str, str]:
    """Parses an action string into an action type and its argument.

    This method is used in Reflexion.

    Args:
        string (str): The action string to be parsed.

    Returns:
        Tuple[str, str]: A tuple containing the action type and argument.
    """
    pattern = r"^(\w+)\[(.+)\]$"
    match = re.match(pattern, string)

    if match:
        action_type = match.group(1)
        argument = match.group(2)
    else:
        action_type = ""
        argument = ""
    return action_type, argument


class ReflexionCoTAgent(BaseAgent):
    """Reflexion with Chain-of-Thought actor.

    Attributes:
        llm (BaseChatModel): The language model used to generate responses.
        benchmark (str): The benchmark.
        reflector (Optional[ReflexionCoTReflector]): An optional reflector module for guided self-reflection.
        **strategy_kwargs (Dict[str, Any]): Additional keyword arguments for the strategy.

    Methods:
        generate(): Generates a response.
        reset(): Resets the agent's state for a new problem-solving session.
    """

    def __init__(
        self,
        llm: BaseChatModel,
        benchmark: str,
        reflector: Optional[ReflexionCoTReflector] = None,
        **strategy_kwargs: Dict[str, Any],
    ) -> None:
        """Initialization."""
        super().__init__()

        self.llm = llm
        self.benchmark = benchmark

        if self.benchmark not in REFLEXION_COT_STRATEGIES:
            raise ValueError(
                f"Unsupported benchmark: {benchmark} for agent ReflexionCoT"
            )
        
        strategy = REFLEXION_COT_STRATEGIES[benchmark]
        self.strategy = strategy(llm=self.llm, reflector=reflector, **strategy_kwargs)

    def generate(
        self,
        question: str,
        key: str,
        examples: str = "",
        prompt: str = "",
        reflect_examples: str = "",
        reflect_prompt: str = "",
        reflect_strategy: str = None,
        additional_keys: Dict[str, str] = {},
        reflect_additional_keys: Dict[str, str] = {},
        fewshot_type: str = "",
        patience: int = 1,
        reset: bool = True,
        **kwargs: Any,
    ) -> List[ReflexionCoTOutput]:
        """Generates a response based on the provided context, question, and key.

        The `generate` method internally calls reflect (if possible), resets the memory,
        and generates a thought, action, and the observation (Finish).

        Args:
            question (str): The question to answer.
            key (str): The key to evaluate the correctness of the answer.
            examples (str, optional): Fewshot examples. Defaults to "".
            prompt (str, optional): Prompt template string. Defaults to "".
            reflect_examples (str, optional): Reflection fewshot examples. Defaults to "".
            reflect_prompt (str, optional): Reflect prompt template string. Defaults to "".
            reflect_strategy (str): The strategy to use for reflection. Can be one of "last_attempt",
                "reflexion", or "last_attempt_and_reflexion", or None. Defaults to None.
            additional_keys (Dict[str, str], optional): Additional keys for the prompt. Defaults to {}.
            reflect_additional_keys (Dict[str, str], optional): Additional keys for the reflect prompt. Defaults to {}.
            fewshot_type (str): The type of few-shot examples to use. Defaults to "".
            patience (int, optional): The patience for the agent. Defaults to 1.
            reset (bool, optional): Whether to reset the agent's memory. Defaults to True.
            **kwargs (Dict[str, Any], optional): Additional keyword arguments for the strategy.

        Returns:
            result (List[ReflexionCoTOutput]): A list of ReflexionCoTOutput containing the thought, action, observation, is_correct, and reflections.
        """

        # Reset.
        if reset:
            self.reset()

        idx, patience_cnt = 0, 0
        out = []
        while not self.strategy.halting_condition(idx=idx, key=key, **kwargs):
            # Reflect if possible.
            reflections: List[str] = []
            reflections_str = ""
            if self.strategy.reflect_condition(
                idx=idx,
                reflect_strategy=reflect_strategy,
                key=key,
            ):
                reflections, reflections_str = self.strategy.reflect(
                    reflect_strategy=reflect_strategy,
                    question=question,
                    examples=reflect_examples,
                    prompt=reflect_prompt,
                    additional_keys=reflect_additional_keys,
                )

            self.strategy.reset(only_scratchpad=True)

            # Think.
            thought = self.strategy.generate(
                question=question,
                examples=examples,
                reflections=reflections_str,
                prompt=prompt,
                additional_keys=additional_keys,
                **kwargs,
            )

            # Act.
            action_type, query = self.strategy.generate_action(
                question=question,
                examples=examples,
                reflections=reflections_str,
                prompt=prompt,
                additional_keys=additional_keys,
                **kwargs,
            )

            # Observe.
            is_correct, obs = self.strategy.generate_observation(
                action_type=action_type,
                query=query,
                key=key,
            )

            out.append(
                ReflexionCoTOutput(
                    **self.strategy.create_output_dict(
                        thought=thought,
                        action_type=action_type,
                        obs=obs,
                        is_correct=is_correct,
                        reflections=reflections,
                    )
                )
            )

            # Increment patience counter.
            if not is_correct:
                patience_cnt += 1
            if patience_cnt == patience:
                break

            idx += 1

        return out

    def reset(self) -> None:
        """Resets the agent's memory and state."""
        self.strategy.reset()


class SelfReflectionCoTAgent(BaseAgent):
    """Reflexion with Chain-of-Thought actor.

    Attributes:
        llm (BaseChatModel): The language model used to generate responses.
        benchmark (str): The benchmark.
        reflector (Optional[ReflexionCoTReflector]): An optional reflector module for guided self-reflection.
        **strategy_kwargs (Dict[str, Any]): Additional keyword arguments for the strategy.

    Methods:
        generate(): Generates a response.
        reset(): Resets the agent's state for a new problem-solving session.
    """

    def __init__(
        self,
        llm: BaseChatModel,
        benchmark: str,
        reflector: Optional[ReflexionCoTReflector] = None,
        **strategy_kwargs: Dict[str, Any],
    ) -> None:
        """Initialization."""
        super().__init__()

        self.llm = llm
        self.benchmark = benchmark

        if self.benchmark not in SELFREFLECTION_COT_STRATEGIES:
            raise ValueError(
                f"Unsupported benchmark: {benchmark} for agent ReflexionCoT"
            )
        
        strategy = SELFREFLECTION_COT_STRATEGIES[benchmark]
        self.strategy = strategy(llm=self.llm, reflector=reflector, **strategy_kwargs)

    def generate(
        self,
        question: str,
        key: str,
        examples: str = "",
        prompt: str = "",
        reflect_examples: str = "",
        reflect_prompt: str = "",
        reflect_strategy: str = None,
        additional_keys: Dict[str, str] = {},
        reflect_additional_keys: Dict[str, str] = {},
        fewshot_type: str = "",
        patience: int = 1,
        reset: bool = True,
        **kwargs: Any,
    ) -> List[ReflexionCoTOutput]:
        """Generates a response based on the provided context, question, and key.

        The `generate` method internally calls reflect (if possible), resets the memory,
        and generates a thought, action, and the observation (Finish).

        Args:
            question (str): The question to answer.
            key (str): The key to evaluate the correctness of the answer.
            examples (str, optional): Fewshot examples. Defaults to "".
            prompt (str, optional): Prompt template string. Defaults to "".
            reflect_examples (str, optional): Reflection fewshot examples. Defaults to "".
            reflect_prompt (str, optional): Reflect prompt template string. Defaults to "".
            reflect_strategy (str): The strategy to use for reflection. Can be one of "last_attempt",
                "reflexion", or "last_attempt_and_reflexion". Defaults to None.
            additional_keys (Dict[str, str], optional): Additional keys for the prompt. Defaults to {}.
            reflect_additional_keys (Dict[str, str], optional): Additional keys for the reflect prompt. Defaults to {}.
            fewshot_type (str): The type of few-shot examples to use. Defaults to "".
            patience (int, optional): The patience for the agent. Defaults to 1.
            reset (bool, optional): Whether to reset the agent's memory. Defaults to True.
            **kwargs (Dict[str, Any], optional): Additional keyword arguments for the strategy.

        Returns:
            result (List[ReflexionCoTOutput]): A list of ReflexionCoTOutput containing the thought, action, observation, is_correct, and reflections.
        """

        # Reset.
        if reset:
            self.reset()

        idx, patience_cnt = 0, 0
        out = []
        while not self.strategy.halting_condition(idx=idx, key=key, **kwargs):
            # Reflect if possible.
            reflections: List[str] = []
            reflections_str = ""
            if self.strategy.reflect_condition(
                idx=idx,
                reflect_strategy=reflect_strategy,
                key=key,
            ):
                reflections, reflections_str = self.strategy.reflect(
                    reflect_strategy=reflect_strategy,
                    question=question,
                    examples=reflect_examples,
                    prompt=reflect_prompt,
                    additional_keys=reflect_additional_keys,
                )

            self.strategy.reset(only_scratchpad=True)

            # Think.
            thought = self.strategy.generate(
                question=question,
                examples=examples,
                reflections=reflections_str,
                prompt=prompt,
                additional_keys=additional_keys,
                **kwargs,
            )

            # Act.
            action_type, query = self.strategy.generate_action(
                question=question,
                examples=examples,
                reflections=reflections_str,
                prompt=prompt,
                additional_keys=additional_keys,
                **kwargs,
            )

            # Observe.
            is_correct, obs = self.strategy.generate_observation(
                action_type=action_type,
                query=query,
                key=key,
            )

            out.append(
                ReflexionCoTOutput(
                    **self.strategy.create_output_dict(
                        thought=thought,
                        action_type=action_type,
                        obs=obs,
                        is_correct=is_correct,
                        reflections=reflections,
                    )
                )
            )

            # Increment patience counter.
            if not is_correct:
                patience_cnt += 1
            if patience_cnt == patience:
                break

            idx += 1

        return out

    def reset(self) -> None:
        """Resets the agent's memory and state."""
        self.strategy.reset()
