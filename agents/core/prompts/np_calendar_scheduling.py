#########
# AGENT #
#########

NPCALLENDARSCHEDULING_FEWSHOT_INSTRUCTION_AGENT = """You are an expert at scheduling meetings. You are given a few constraints on the existing schedule of each participant, the meeting duration, and possibly some preferences on the meeting time. Note there exists a solution that works with existing schedule of every participant.

Here are a few example tasks and solutions. Pay attention to how the solution is structured.
{examples}
(END OF EXAMPLES)"""

# {reflections}

# Question: {question}{scratchpad}"""


NPCALLENDARSCHEDULING_ZEROSHOT_INSTRUCTION_AGENT = """You are an expert meeting scheduler. You are given:
- Few constraints on each participant's existing schedule.
- Meeting duration required.
- Preferences for meeting times (if any).

Assumption: A feasible solution exists that accommodates all participants' schedules.

Propose a meeting time that works for everyone by reasoning through it step by step.

Your response should be formatted as follows:
Thought: Let's think step by step. (Explain your reasoning in detail)
Action: Finish[Day, HH:MM - HH:MM]
"""

# {reflections}

# Question: {question}{scratchpad}"""
