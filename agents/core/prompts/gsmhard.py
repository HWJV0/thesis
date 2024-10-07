#########
# AGENT #
#########

GSMHARD_FEWSHOT_INSTRUCTION_AGENT = """You are an expert at solving math word problems with large numbers. Solve a math question task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task.

Here are a few example tasks and solutions. Pay attention to how the solution is structured.
{examples}
(END OF EXAMPLES)
"""

GSMHARD_ZEROSHOT_INSTRUCTION_AGENT = """You are an expert at solving math word problems with large numbers. Solve a math question task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task."""

GSMHARD_POT_FEWSHOT_INSTRUCTION_AGENT = """"You are an expert at solving math word problems and programming to implement the solutions. Solve a math question task by having a Thought to reason logically and conceptually. Then, Finish with your answer as as executable Python code, using the given numbers from the question.

Here are a few example tasks and solutions. Pay attention to how the solution is structured.
{examples}
(END OF EXAMPLES)
"""