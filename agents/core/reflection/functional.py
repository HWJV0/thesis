"""Functional module for Reflexion."""

from typing import Dict, List

import tiktoken

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages.human import HumanMessage
from langchain_core.messages.system import SystemMessage
from langchain_core.messages.ai import AIMessage
from langchain_core.prompts.prompt import PromptTemplate
from tiktoken.core import Encoding

from agents.core.reflection.prompts.general import (
    REFLECTION_HEADER,
    INTERMODEL_REFLECTION_HEADER
)
from agents.utils.parse import remove_newline

def _format_reflections(reflections: List[str], header: str = REFLECTION_HEADER) -> str:
    """Formats a list of reflection strings into a single formatted string.

    Args:
        reflections (List[str]): A list of reflection strings to be formatted.
        header (str, optional): A header to prepend to the formatted reflections. Defaults to REFLECTION_HEADER.

    Returns:
        str: The formatted string of reflections.
    """
    # Return formatted reflections if not empty.
    if reflections:
        return (
            header + "Reflections:\n- " + "\n- ".join([r.strip() for r in reflections])
        )
    else:
        return ""

def _build_cot_agent_prompt(
    examples: str,
    # reflections: str,
    # question: str,
    # scratchpad: str,
    prompt: str,
    additional_keys: Dict[str, str] = {},
) -> str:
    """Constructs a ReflexionCoT prompt template for the agent.

    This function formats a predefined prompt template (REFLEXION_COT_INSTRUCTION or
    REFLEXION_COT_INSTRUCTION_NO_CONTEXT) with examples,
    the provided question, and a scratchpad.

    Args:
        examples (str): Example inputs for the prompt template.
        reflections (List[str]): Existing list of reflections.
        question (str): The question being addressed.
        scratchpad (str): The scratchpad content related to the question.
        prompt (str, optional): Prompt template string.
        additional_keys (Dict[str, str]): Additional keys to format the prompt. Defaults to {}.

    Returns:
        str: A formatted prompt template ready for use.
    """
    prompt = PromptTemplate(
        input_variables=[
            "examples",
            # "reflections",
            # "question",
            # "scratchpad",
        ]
        + list(additional_keys.keys()),
        template=prompt,
    ).format(
        examples=examples,
        # reflections=reflections,
        # question=question,
        # scratchpad=scratchpad,
        **additional_keys,
    )

    return prompt


def _prompt_cot_agent(
    llm: BaseChatModel,
    examples: str,
    reflections: str,
    question: str,
    scratchpad: str,
    prompt: str,
    additional_keys: Dict[str, str] = {},
) -> str:
    """Generates a CoT prompt for thought and action.

    Used with ReflexionCoT.

    Args:
        llm (BaseChatModel): The language model to be used for generating the reflection.
        examples (str): Example inputs for the prompt template.
        reflections (List[str]): Existing list of reflections.
        question (str): The question being addressed.
        scratchpad (str): The scratchpad content related to the question.
        prompt (str, optional): Prompt template string.
        additional_keys (Dict[str, str]): Additional keys to format the prompt. Defaults to {}.

    Returns:
        str: The generated reflection prompt.
    """
    prompt = _build_cot_agent_prompt(
        examples=examples,
        # reflections=reflections,
        # question=question,
        # scratchpad=scratchpad,
        prompt=prompt,
        additional_keys=additional_keys,
    )

    out = llm(
        [
            SystemMessage(
                content=prompt #+ f"\n\n{reflections}\n\nQuestion: {question}{scratchpad}",
            ),
            HumanMessage(
                content=f"{reflections}\n\nQuestion: {question}{scratchpad}"
            ),
        ]
    ).content
    assert isinstance(out, str)
    return out


def _build_cot_reflection_prompt(
    examples: str,
    # question: str,
    # scratchpad: str,
    prompt: str,
    additional_keys: Dict[str, str] = {},
) -> str:
    """Constructs a ReflexionCoT prompt template for reflection.

    Args:
        examples (str): Example inputs for the prompt template.
        question (str): The question being addressed.
        scratchpad (str): The scratchpad content related to the question.
        prompt (str, optional): Prompt template string.
        additional_keys (Dict[str, str]): Additional keys to format the prompt. Defaults to {}.

    Returns:
        str: A formatted prompt template ready for use.
    """
    prompt = PromptTemplate(
        input_variables=[
            "examples",
            # "question",
            # "scratchpad"
        ]
        + list(additional_keys.keys()),
        template=prompt,
    ).format(
        examples=examples,
        # question=question,
        # scratchpad=scratchpad,
        **additional_keys,
    )

    return prompt


def _prompt_cot_reflection(
    llm: BaseChatModel,
    examples: str,
    question: str,
    scratchpad: str,
    prompt: str,
    additional_keys: Dict[str, str] = {},
) -> str:
    """Generates a reflection prompt.

    Used with ReflexionCoT.

    Args:
        llm (BaseChatModel): The language model to be used for generating the reflection.
        examples (str): Example inputs for the prompt template.
        question (str): The question being addressed.
        scratchpad (str): The scratchpad content related to the question.
        prompt (str, optional): Prompt template string.
        additional_keys (Dict[str, str]): Additional keys to format the prompt. Defaults to {}.

    Returns:
        str: The generated reflection prompt.
    """
    prompt = _build_cot_reflection_prompt(
        examples=examples,
        # question=question,
        # scratchpad=scratchpad,
        prompt=prompt,
        additional_keys=additional_keys,
    )
    out = llm(
        [
            SystemMessage(
                content=prompt # + f"\n\nPrevious Trial:\nQuestion: {question}{scratchpad}\n\nReflection:",
            ),
            HumanMessage(
                content=f"Previous Trial:\nQuestion: {question}{scratchpad}\n\nReflection:"
            )
        ]
    ).content
    assert isinstance(out, str)
    return out


def cot_reflect_last_attempt(scratchpad: str) -> List[str]:
    """Performs a reflection based on the last attempt (scratchpad).

    Used with ReflexionCoT.

    Args:
        question (str): The question associated with the last attempt.
        scratchpad (str): The scratchpad content from the last attempt.

    Returns:
        List[str]: A list with the scratchpad content.
    """
    return [scratchpad]


def cot_reflect_reflexion(
    llm: BaseChatModel,
    reflections: List[str],
    examples: str,
    question: str,
    scratchpad: str,
    prompt: str,
    additional_keys: Dict[str, str] = {},
) -> List[str]:
    """Perform reflexion-based reflecting.

    Used with ReflexionCoT. This function uses a language model to generate a new reflection based on the provided context, question,
    and scratchpad. The new reflection is added to the existing list of reflections.

    Args:
        llm (BaseChatModel): The language model used for generating the reflection.
        reflections (List[str]): Existing list of reflections.
        examples (str): Example inputs for the prompt template.
        question (str): The question being addressed.
        scratchpad (str): The scratchpad content related to the question.
        prompt (str, optional): Prompt template string.
        additional_keys (Dict[str, str]): Additional keys to format the prompt. Defaults to {}

    Returns:
        List[str]: An updated list of reflections.
    """
    new_reflection = _prompt_cot_reflection(
        llm=llm,
        examples=examples,
        question=question,
        scratchpad=scratchpad,
        prompt=prompt,
        additional_keys=additional_keys,
    )
    new_reflection = remove_newline(new_reflection)
    reflections += [new_reflection]
    return reflections


# def cot_reflect_last_attempt_and_reflexion(
#     llm: BaseChatModel,
#     examples: str,
#     question: str,
#     scratchpad: str,
#     prompt: str,
#     additional_keys: Dict[str, str] = {},
# ) -> List[str]:
#     """Performs reflection with the reflection of the last attempt and reflexion.

#     Used with ReflexionCoT.

#     Args:
#         llm (BaseChatModel): The language model used for generating the new reflection.
#         examples (str): Example inputs for the prompt template.
#         question (str): The question being addressed.
#         scratchpad (str): The scratchpad content related to the question.
#         context (Optional[str]): The context of the conversation or query. Defaults to None.
#         prompt (str, optional): Prompt template string.
#         additional_keys (Dict[str, str]): Additional keys to format the prompt. Defaults to {}

#     Returns:
#         List[str]: A list with the new reflections.
#     """
#     reflections = [
#         remove_newline(
#             _prompt_cot_reflection(
#                 llm=llm,
#                 examples=examples,
#                 question=question,
#                 scratchpad=scratchpad,
#                 prompt=prompt,
#                 additional_keys=additional_keys,
#             )
#         )
#     ]
#     return reflections


def cot_reflect(
    reflect_strategy: str,
    llm: BaseChatModel,
    reflections: List[str],
    examples: str,
    question: str,
    scratchpad: str,
    prompt: str,
    additional_keys: Dict[str, str] = {},
) -> List[str]:
    """Performs reflection based on a specified strategy using provided context, question, and scratchpad.

    Used with ReflexionCoT. This function orchestrates different types of reflections based on the strategy provided. It either reflects on the
    last attempt, generates a new reflexion, or combines both approaches. Depending on the strategy, it either uses
    the existing reflections, modifies them, or generates new reflections using the provided language model.

    Args:
        reflect_strategy (str): The reflection strategy to be used ('last_attempt', 'reflexion', or 'last_attempt_and_reflexion').
        llm (BaseChatModel): The language model used for generating new reflections.
        reflections (List[str]): A list of existing reflections.
        examples (str): Example inputs for the prompt template.
        question (str): The question being addressed.
        scratchpad (str): The scratchpad content related to the question.
        prompt (str): Prompt template string.
        additional_keys (Dict[str, str], optional): Additional keys to be passed to the prompt template. Defaults to {}

    Returns:
        List[str]: A list of reflections.

    Raises:
        NotImplementedError: If an unknown reflection strategy is specified.

    Strategy-Specific Parameters:
        - "last_attempt": This strategy uses only 'question' and 'scratchpad'. The 'reflections' list is updated with the current scratchpad.
        - "reflexion": This strategy uses all the parameters. It adds a new reflexion generated by the language model to the 'reflections' list.
        - "last_attempt_and_reflexion": This strategy combines the 'last_attempt' and 'reflexion' strategies.
          It first formats the last attempt using 'question' and 'scratchpad', then adds a new reflexion using all the parameters.
    """
    # if reflect_strategy == "last_attempt":
    #     reflections = cot_reflect_last_attempt(scratchpad)
    if reflect_strategy == "reflexion":
        reflections = cot_reflect_reflexion(
            llm=llm,
            reflections=reflections,
            examples=examples,
            question=question,
            scratchpad=scratchpad,
            prompt=prompt,
            additional_keys=additional_keys,
        )
    # elif reflect_strategy == "last_attempt_and_reflexion":
    #     reflections = cot_reflect_last_attempt_and_reflexion(
    #         llm=llm,
    #         examples=examples,
    #         question=question,
    #         scratchpad=scratchpad,
    #         prompt=prompt,
    #         additional_keys=additional_keys,
    #     )
    else:
        raise NotImplementedError(f"Unknown reflection strategy: {reflect_strategy}.")

    return reflections
