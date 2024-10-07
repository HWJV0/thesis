NPCALLENDARSCHEDULING_FEWSHOT_EXAMPLES_AGENT_COT = """
Question: You need to schedule a meeting for Roger, Karen and Dorothy for half an hour between the work hours of 9:00 to 17:00 on Monday.
Here are the existing schedules for everyone during the day:
Roger's calendar is wide open the entire day.
Karen has meetings on Monday during 10:00 to 10:30, 11:30 to 12:00, 12:30 to 13:00, 14:00 to 15:00, 15:30 to 16:00;
Dorothy is busy on Monday during 9:00 to 10:00, 10:30 to 11:00, 11:30 to 12:00, 12:30 to 13:00, 14:00 to 15:30, 16:00 to 17:00;

You would like to schedule the meeting at their earliest availability.
Find a time that works for everyone's schedule and constraints.

Thought: Let's think step by step. First, we need a half-hour slot when none of the three have other commitments. Roger is free all day, so we consider Karen and Dorothy's schedules. The overlapping busy times to avoid are from 10:00 to 10:30, 11:30 to 12:00, 12:30 to 13:00, 14:00 to 15:00, and 15:30 to 16:00. The first available slot for all three, considering these constraints, is right after Dorothy's 10:30 meeting ends and before Karen's 11:30 meeting begins.
Action: Finish[Monday, 11:00 - 11:30]


Question: You need to schedule a meeting for Douglas, Lawrence and Isabella for half an hour between the work hours of 9:00 to 17:00 on Monday.
Here are the existing schedules for everyone during the day:
Douglas has meetings on Monday during 12:00 to 12:30, 15:00 to 15:30;
Lawrence has meetings on Monday during 10:30 to 12:00, 13:00 to 13:30, 14:00 to 14:30, 15:30 to 16:00;
Isabella is busy on Monday during 9:00 to 12:30, 13:30 to 17:00;

Find a time that works for everyone's schedule and constraints.

Thought: Let's think step by step. To find a suitable meeting time, we must find a gap when all three are free. Douglas and Isabella are both busy until 12:30. Lawrence is free after his 12:00 meeting and before his 13:00 meeting. The only common free time between their commitments is right after Isabella and Douglas finish their overlapping engagements.
Action: Finish[Monday, 12:30 - 13:00]


Question: You need to schedule a meeting for Joshua, Denise and Jeremy for one hour between the work hours of 9:00 to 17:00 on Monday.
Here are the existing schedules for everyone during the day:
Joshua is busy on Monday during 10:00 to 10:30, 12:00 to 12:30, 14:00 to 14:30, 15:00 to 15:30;
Denise's calendar is wide open the entire day.
Jeremy has meetings on Monday during 9:30 to 10:30, 12:00 to 13:00, 13:30 to 14:00, 14:30 to 15:00, 15:30 to 16:00, 16:30 to 17:00;

Find a time that works for everyone's schedule and constraints.

Thought: Let's think step by step. We are looking for a one-hour block. Joshua is free after his 10:00 meeting and before his 12:00 meeting. Jeremy is free right after his 9:30 meeting until 12:00. Since Denise is available any time, the earliest time all can meet without any overlap from other commitments is right after Joshua's and Jeremy's morning meetings.
Action: Finish[Monday, 10:30 - 11:30]


Question: You need to schedule a meeting for Alan, Elizabeth and Denise for half an hour between the work hours of 9:00 to 17:00 on Monday.
Here are the existing schedules for everyone during the day:
Alan has blocked their calendar on Monday during 13:00 to 13:30, 14:00 to 14:30;
Elizabeth is busy on Monday during 9:00 to 9:30, 11:00 to 11:30;
Denise has blocked their calendar on Monday during 9:00 to 10:00, 10:30 to 11:30, 12:30 to 13:00, 13:30 to 14:00, 14:30 to 16:00, 16:30 to 17:00;

You would like to schedule the meeting at their earlist availability.
Find a time that works for everyone's schedule and constraints.

Thought: Let's think step by step. To find a slot for this meeting, we need a half-hour period when none have other engagements. Between Alan's and Denise's schedules, the gaps are fairly limited. The earliest time slot where all three have no conflicts is after Elizabeth's early morning meeting and before her next engagement.
Action: Finish[Monday, 10:00 - 10:30]


Question: You need to schedule a meeting for Mason, Bruce and Christopher for half an hour between the work hours of 9:00 to 17:00 on Monday.
Here are the existing schedules for everyone during the day:
Mason has meetings on Monday during 9:30 to 10:00, 11:00 to 11:30, 14:30 to 15:00, 16:30 to 17:00;
Bruce is free the entire day.
Christopher is busy on Monday during 9:30 to 10:30, 11:30 to 12:30, 15:00 to 17:00;

Mason would rather not meet on Monday before 12:30. Find a time that works for everyone's schedule and constraints.

Thought: Let's think step by step. Considering Mason's preference and everyone's schedules, we need to find a free half-hour after 12:30. The only time slot that aligns with this preference and where all are free is right after Mason's morning restriction ends and before Christopher's afternoon engagements begin.
Action: Finish[Monday, 12:30 - 13:00]
"""
