#########
# AGENT #
#########

GSM8K_FEWSHOT_INSTRUCTION_AGENT = """You are an expert at solving math word problems. Solve a math question task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Thought can reason about the current situation. Your answer should be an integer, written as a whole number without any commas or decimal points. Finish[answer] returns the answer and finishes the task.

Here are a few example tasks and solutions. Pay attention to how the solution is structured.
{examples}
(END OF EXAMPLES)
"""

GSM8K_ZEROSHOT_INSTRUCTION_AGENT = """You are an expert at solving math word problems. Solve a math question task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Thought can reason about the current situation. Your answer should be an integer, written as a whole number without any commas or decimal points. Finish[answer] returns the answer and finishes the task."""
# Your response should be formatted as:
# Thought: Let's think step by step.
# Action: Finish[integer
# # ```
# # python
# # <code>
# # ```
# # ]




# """Solve a math question task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task.

# # Here are some examples:
# # {examples}
# # (END OF EXAMPLES)

# # {reflections}

# # Question: {question}{scratchpad}"""


# GSM8K_ZEROSHOT_INSTRUCTION_AGENT = """You are an expert at solving math word problems.

# Solve the following problem by reasoning through it step by step.

# Your response should be formatted as:
# Thought: Let's think step by step.
# Action: Finish[<answer>]"""

# GSM8K_POT_FEWSHOT_INSTRUCTION_AGENT = """"You are an expert at solving math word problems and programming to implement the solutions

# Solve the following problem by reasoning through it step by step logically and conceptually without referring to specific numbers. Then, execute your plan using the given numbers and provide the final answer as executable Python code.

# Your response should be formatted as:
# Thought: Let's think step by step. (Explain your reasoning in detail)
# Action: Finish[
# ```
# python
# <code>
# ```
# ]

# Here are a few examples:
# {examples}
# (END OF EXAMPLES)"""


# GSM8K_POT_ZEROSHOT_INSTRUCTION_AGENT = """"You are an expert at solving math word problems and programming to implement the solutions

# Solve the following problem by reasoning through it step by step logically and conceptually without referring to specific numbers. Then, execute your plan using the given numbers and provide the final answer as executable Python code.

# Your response should be formatted as:
# Thought: Let's think step by step. (Explain your reasoning in detail)
# Action: Finish[
# ```
# python
# <code>
# ```
# ]"""
