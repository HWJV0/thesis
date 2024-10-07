###########
# HEADERS #
###########

# REFLECTION_HEADER = "You have attempted to answer following question before and failed. The following reflection(s) give a plan to avoid failing to answer the question in the same way you did previously. Use them to improve your strategy of correctly answering the given question.\n"
# REFLECTION_HEADER = "You have previously attempted to answer the following question. The following reflections analyze your attempt and offer strategies to ensure your answer is correct. Use these insights to refine your approach and, if necessary, correct your response.\n"
REFLECTION_HEADER = "You have attempted to answer the following question before. Below are reflection(s) that offer strategies to critically evaluate and refine your approach. Use these insights to assess and, if necessary, correct your answer.\n"

INTERMODEL_REFLECTION_HEADER = """Someone else has attempted to answer the following question. Below are reflection(s) that offer strategies to critically evaluate and refine the original answer. Use these insights to assess and, if necessary, correct the original answer.\n"""

############
# FEW-SHOT #
############

FEWSHOT_REFLECT_INSTRUCTION_NEGATIVE = """You are an advanced reasoning agent that can improve based on self-reflection. You will be given a previous reasoning trial in which you were given a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[answer]. In a few sentences, diagnose a possible reason for failure or phrasing discrepancy and devise a new, concise, high-level plan that aims to mitigate the same failure. Use complete sentences.

Here are a few examples. Pay attention to how the reflection is structured.
{examples}
(END OF EXAMPLES)"""

# Previous Trial:
# Question: {question}{scratchpad}

# Reflection:"""

FEWSHOT_REFLECT_INSTRUCTION_CRITICAL = """You are an advanced reasoning agent that can improve based on self-reflection. You will be given a previous reasoning trial in which you were given a question to answer. Critically evaluate if your answer with Finish[answer] is correct. Identify any areas that might benefit from correction and develop a concise, high-level plan to correct your approach if needed. Use complete sentences.

Here are a few examples. Pay attention to how the reflection is structured.
{examples}
(END OF EXAMPLES)"""

# Previous Trial:
# Question: {question}{scratchpad}

# Reflection:"""

FEWSHOT_INTERMODEL_REFLECT_INSTRUCTION_CRITICAL = """You are an advanced reasoning agent that can improve another model's performance through critical evaluation. You will be provided with a previous reasoning trial where another model attempted to answer a question. Critically assess whether the other model's answer, marked with Finish[answer], is correct. Identify any potential weaknesses or areas for improvement and develop a concise, high-level plan to enhance the original model's approach. Use complete sentences.

Here are a few examples. Pay attention to how the reflection is structured.
{examples}
(END OF EXAMPLES)
"""


#############
# ZERO-SHOT #
#############

ZEROSHOT_REFLECT_INSTRUCTION_NEGATIVE = """You are an advanced reasoning agent that can improve based on self-reflection. You will be given a previous reasoning trial in which you were given a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[answer]. In a few sentences, diagnose a possible reason for failure or phrasing discrepancy and devise a new, concise, high-level plan that aims to mitigate the same failure. Use complete sentences."""

# Previous Trial:
# Question: {question}{scratchpad}

# Reflection:"""

ZEROSHOT_REFLECT_INSTRUCTION_CRITICAL = """You are an advanced reasoning agent that can improve based on self-reflection. You will be given a previous reasoning trial in which you were given a question to answer. Critically evaluate if your answer with Finish[answer] is correct. Identify any areas that might benefit from correction and develop a concise, high-level plan to correct your approach if needed. Use complete sentences."""

# Previous Trial:
# Question: {question}{scratchpad}

# Reflection:"""

ZEROSHOT_INTERMODEL_REFLECT_INSTRUCTION_CRITICAL = """You are an advanced reasoning agent tasked with enhancing another's performance through critical evaluation. You will be provided with a previous reasoning attempt where someone else attempted to answer a question. Critically assess whether their answer, marked with Finish[answer], is correct. Identify any potential weaknesses or areas for improvement and develop a concise, high-level plan to enhance the original approach. Use complete sentences."""
