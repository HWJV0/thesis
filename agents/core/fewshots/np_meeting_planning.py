NPMEETINGPLANNING_FEWSHOT_EXAMPLES_AGENT_COT = """You are visiting San Francisco for the day and want to meet as many friends as possible. Solve the problem by considering various different schedules and picking the best one to optimize your goals.

Question: Travel distances (in minutes):
Haight-Ashbury to Chinatown: 19.
Chinatown to Haight-Ashbury: 19.

Constraints: You arrive at Haight-Ashbury at 9:00AM. Joseph will be at Chinatown from 2:45PM to 7:00PM.

You'd like to meet Joseph for a minimum of 30 minutes.

Thought: Let's think step by step. You are visiting San Francisco for the day and aim to meet as many friends as possible. Your day starts at Haight-Ashbury at 9:00AM. To meet Joseph, you need to be in Chinatown between 2:45PM and 7:00PM. The travel time from Haight-Ashbury to Chinatown is 19 minutes, so you will arrive in Chinatown at 9:19AM. Since Joseph is only available starting at 2:45PM, you will wait in Chinatown until his arrival time. This ensures you meet him for the required 30 minutes without conflicting with other potential meetings.
Action: Finish[You start at Haight-Ashbury at 9:00AM. You travel to Chinatown in 19 minutes and arrive at 9:19AM. You wait until 2:45PM. You meet Joseph for 30 minutes from 2:45PM to 3:15PM.]


Question: You are visiting San Francisco for the day and want to meet as many friends as possible. Solve the problem by considering various different schedules and picking the best one to optimize your goals

Travel distances (in minutes):
Marina District to Nob Hill: 12.
Nob Hill to Marina District: 11.

Constraints: You arrive at Marina District at 9:00AM. Timothy will be at Nob Hill from 7:45AM to 4:30PM.

You'd like to meet Timothy for a minimum of 120 minutes.

Thought: Let's think step by step. You are visiting San Francisco for the day and want to maximize the number of friends you meet. You start your day at Marina District at 9:00AM. To meet Timothy at Nob Hill, you need to consider the travel time of 12 minutes. Departing at 9:00AM, you arrive at Nob Hill by 9:12AM. Timothy is available until 4:30PM, giving you ample time to schedule a 120-minute meeting. By meeting Timothy from 9:12AM to 11:12AM, you efficiently utilize the morning hours, leaving the rest of the day open to meet other friends.
Action: Finish[You start at Marina District at 9:00AM. You travel to Nob Hill in 12 minutes and arrive at 9:12AM. You meet Timothy for 120 minutes from 9:12AM to 11:12AM.]


Question: You are visiting San Francisco for the day and want to meet as many friends as possible. Solve the problem by considering various different schedules and picking the best one to optimize your goals

Travel distances (in minutes):
Mission District to Golden Gate Park: 17.
Golden Gate Park to Mission District: 17.

Constraints: You arrive at Mission District at 9:00AM. Elizabeth will be at Golden Gate Park from 4:00PM to 7:30PM.

You'd like to meet Elizabeth for a minimum of 60 minutes.

Thought: Let's think step by step. You are visiting San Francisco for the day with the goal of meeting as many friends as possible. Your day begins at Mission District at 9:00AM. To meet Elizabeth at Golden Gate Park, you need to account for a 17-minute travel time. Departing at 9:00AM, you arrive at Golden Gate Park by 9:17AM. However, Elizabeth is only available starting at 4:00PM. Therefore, you will wait at Golden Gate Park until 4:00PM to meet her for the required 60 minutes, from 4:00PM to 5:00PM. This scheduling ensures you meet Elizabeth without overlapping with other potential meetings.
Action: Finish[You start at Mission District at 9:00AM. You travel to Golden Gate Park in 17 minutes and arrive at 9:17AM. You wait until 4:00PM. You meet Elizabeth for 60 minutes from 4:00PM to 5:00PM.]


Question: You are visiting San Francisco for the day and want to meet as many friends as possible. Solve the problem by considering various different schedules and picking the best one to optimize your goals

Travel distances (in minutes):
Mission District to Bayview: 15.
Bayview to Mission District: 13.

Constraints: You arrive at Mission District at 9:00AM. Jeffrey will be at Bayview from 9:45PM to 10:15PM.

You'd like to meet Jeffrey for a minimum of 15 minutes.

Thought: Let's think step by step. You are visiting San Francisco for the day with the objective of meeting as many friends as possible. Your day starts at Mission District at 9:00AM. To meet Jeffrey at Bayview, you need to consider a 15-minute travel time. Departing at 9:00AM, you arrive at Bayview by 9:15AM. Since Jeffrey is only available from 9:45PM to 10:15PM, you will wait at Bayview until 9:45PM to meet him for the required 15 minutes, from 9:45PM to 10:00PM. This ensures you meet Jeffrey without conflicting with other potential engagements throughout the day.
Action: Finish[You start at Mission District at 9:00AM. You travel to Bayview in 15 minutes and arrive at 9:15AM. You wait until 9:45PM. You meet Jeffrey for 15 minutes from 9:45PM to 10:00PM.]


Question: You are visiting San Francisco for the day and want to meet as many friends as possible. Solve the problem by considering various different schedules and picking the best one to optimize your goals

Travel distances (in minutes):
Alamo Square to Mission District: 10.
Mission District to Alamo Square: 11.

Constraints: You arrive at Alamo Square at 9:00AM. Joshua will be at Mission District from 7:45PM to 9:30PM.

You'd like to meet Joshua for a minimum of 60 minutes.

Thought: Let's think step by step. You are visiting San Francisco for the day with the aim of meeting as many friends as possible. Your day begins at Alamo Square at 9:00AM. To meet Joshua at Mission District, you need to account for an 10-minute travel time. Departing at 9:00AM, you arrive at Mission District by 9:10AM. Joshua is available from 7:45PM to 9:30PM. To fulfill the 60-minute meeting requirement, you will wait at Mission District until 7:45PM and meet Joshua from 7:45PM to 8:45PM. This scheduling allows you to meet Joshua without overlapping with other meetings and optimizes your day for meeting multiple friends.
Action: Finish[You start at Alamo Square at 9:00AM. You travel to Mission District in 10 minutes and arrive at 9:10AM. You wait until 7:45PM. You meet Joshua for 60 minutes from 7:45PM to 8:45PM.]
"""
