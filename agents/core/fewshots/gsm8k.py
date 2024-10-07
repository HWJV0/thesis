GSM8K_FEWSHOT_EXAMPLES_AGENT_COT = """Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny? Solve the math question.
Thought: Let's think step by step. Jason initially had 20 lollipops. After giving some to Denny, he had 12 lollipops left. To find how many he gave to Denny, we subtract the remaining lollipops from the initial amount: 20 - 12 = 8. Therefore, Jason gave 8 lollipops to Denny.
Action: Finish[8]


Question: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today? Solve the math question.
Thought: Let's think step by step. Initially, there were 15 trees in the grove. After the workers planted some more, there were 21 trees. The number of trees planted is the difference between the final and initial number of trees: 21 - 15 = 6. Therefore, the workers planted 6 trees today.
Action: Finish[6]


Question: There were nine computers in the server room. Five more computers were installed each day, from Monday to Thursday. How many computers are now in the server room? Solve the math question.
Thought: Let's think step by step. Initially, there were 9 computers in the server room. From Monday to Thursday, which is 4 days, 5 computers were installed each day. The total number of computers installed is 5 * 4 = 20. Adding this to the initial 9 computers, the total number of computers in the server room is 9 + 20 = 29.
Action: Finish[29]


Question: Michael had 58 golf balls. On Tuesday, he lost 23 golf balls. On Wednesday, he lost 2 more. How many golf balls did he have at the end of Wednesday? Solve the math question.
Thought: Let's think step by step. Michael started with 58 golf balls. He lost 23 golf balls on Tuesday, leaving him with 58 - 23 = 35 golf balls. On Wednesday, he lost 2 more, so we subtract 2 from 35, which gives 35 - 2 = 33. Therefore, he had 33 golf balls at the end of Wednesday.
Action: Finish[33]


Question: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot? Solve the math question.
Thought: Let's think step by step. Initially, there are 3 cars in the parking lot. When 2 more cars arrive, we add the 2 cars to the original 3 cars, giving us 3 + 2 = 5 cars in total.
Action: Finish[5]


Question: Olivia has $23. She bought five bagels for $3 each. How much money does she have left? Solve the math question.
Thought: Let's think step by step. Olivia started with $23. She bought 5 bagels, each costing $3. The total cost of the bagels is 5 * 3 = $15. To find how much money she has left, we subtract the cost of the bagels from her initial amount: 23 - 15 = $8.
Action: Finish[8]


Question: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total? Solve the math question.
Thought: Let's think step by step. Leah had 32 chocolates, and her sister had 42 chocolates. Together, they had 32 + 42 = 74 chocolates. They ate 35 chocolates, so the number of chocolates they have left is 74 - 35 = 39.
Action: Finish[39]"""

# GSM8K_FEWSHOT_EXAMPLES_POT = """Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
# # Python code, return answer
# jason_lollipops_initial = 20
# jason_lollipops_after = 12
# denny_lollipops = jason_lollipops_initial - jason_lollipops_after
# answer = denny_lollipops

# ---

# Question: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
# # Python code, return answer
# trees_initial = 15
# trees_after = 21
# trees_added = trees_after - trees_initial
# answer = trees_added

# ---

# Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
# # Python code, return answer
# toys_initial = 5
# mom_toys = 2
# dad_toys = 2
# total_received = mom_toys + dad_toys
# total_toys = toys_initial + total_received
# answer = total_toys

# ---

# Question: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?
# # Python code, return answer
# computers_initial = 9
# computers_per_day = 5
# num_days = 4  # 4 days between monday and thursday
# computers_added = computers_per_day * num_days
# computers_total = computers_initial + computers_added
# answer = computers_total

# ---

# Question: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?
# # Python code, return answer
# golf_balls_initial = 58
# golf_balls_lost_tuesday = 23
# golf_balls_lost_wednesday = 2
# golf_balls_left = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday
# answer = golf_balls_left

# ---

# Question: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
# # Python code, return answer
# cars_initial = 3
# cars_arrived = 2
# total_cars = cars_initial + cars_arrived
# answer = total_cars

# ---

# Question: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
# # Python code, return answer
# money_initial = 23
# bagels = 5
# bagel_cost = 3
# money_spent = bagels * bagel_cost
# money_left = money_initial - money_spent
# answer = money_left

# ---

# Question: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
# # Python code, return answer
# leah_chocolates = 32
# sister_chocolates = 42
# total_chocolates = leah_chocolates + sister_chocolates
# chocolates_eaten = 35
# chocolates_left = total_chocolates - chocolates_eaten
# answer = chocolates_left"""


# GSM8K_FEWSHOT_EXAMPLES_COT_POT = """Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
# Thought: Let's think step by step. Jason had 20 lollipops initially and now he has 12 lollipops. So, he must have given 20 - 12 = 8 lollipops to Denny.
# Action: Finish[
# ```python
# jason_lollipops_initial = 20
# jason_lollipops_after = 12
# denny_lollipops = jason_lollipops_initial - jason_lollipops_after
# answer = denny_lollipops
# ```
# ]

# ---

# Question: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
# Thought: Let's think step by step. There were initially 15 trees and after planting, there are 21 trees. So, the number of trees planted is 21 - 15 = 6.
# Action: Finish[
# ```python
# trees_initial = 15
# trees_after = 21
# trees_added = trees_after - trees_initial
# answer = trees_added
# ```
# ]

# ---

# Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
# Thought: Let's think step by step. Shawn had 5 toys initially, and he got 2 toys from his mom and 2 toys from his dad. So, the total number of toys he has now is 5 + 2 + 2 = 9.
# Action: Finish[
# ```python
# toys_initial = 5
# mom_toys = 2
# dad_toys = 2
# total_received = mom_toys + dad_toys
# total_toys = toys_initial + total_received
# answer = total_toys
# ```
# ]

# ---

# Question: There were nine computers in the server room. Five more computers were installed each day, from Monday to Thursday. How many computers are now in the server room?
# Thought: Let's think step by step. Initially, there were 9 computers. Five more computers were added each day from Monday to Thursday, which is 4 days. So, the total number of computers added is 5 * 4 = 20. Therefore, the total number of computers now is 9 + 20 = 29.
# Action: Finish[
# ```python
# computers_initial = 9
# computers_per_day = 5
# num_days = 4  # 4 days between Monday and Thursday
# computers_added = computers_per_day * num_days
# computers_total = computers_initial + computers_added
# answer = computers_total
# ```
# ]

# ---

# Question: Michael had 58 golf balls. On Tuesday, he lost 23 golf balls. On Wednesday, he lost 2 more. How many golf balls did he have at the end of Wednesday?
# Thought: Let's think step by step. Michael initially had 58 golf balls. He lost 23 golf balls on Tuesday and 2 more on Wednesday. So, the total number of golf balls lost is 23 + 2 = 25. Therefore, the number of golf balls he has left is 58 - 25 = 33.
# Action: Finish[
# ```python
# golf_balls_initial = 58
# golf_balls_lost_tuesday = 23
# golf_balls_lost_wednesday = 2
# golf_balls_left = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday
# answer = golf_balls_left
# ```
# ]


# ---

# Question: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
# Thought: Let's think step by step. Initially, there are 3 cars in the parking lot. When 2 more cars arrive, the total number of cars is 3 + 2 = 5.
# Action: Finish[
# ```python
# cars_initial = 3
# cars_arrived = 2
# total_cars = cars_initial + cars_arrived
# answer = total_cars
# ```
# ]

# ---

# Question: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
# Thought: Let's think step by step. Olivia had $23 initially. She bought 5 bagels for $3 each. The total cost of the bagels is 5 * 3 = $15. So, the money she has left is 23 - 15 = $8.
# Action: Finish[
# ```python
# money_initial = 23
# bagels = 5
# bagel_cost = 3
# money_spent = bagels * bagel_cost
# money_left = money_initial - money_spent
# answer = money_left
# ```
# ]

# ---

# Question: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
# Thought: Let's think step by step. Leah had 32 chocolates and her sister had 42 chocolates. Together they had 32 + 42 = 74 chocolates. They ate 35 chocolates, so the number of chocolates left is 74 - 35 = 39.
# Action: Finish[
# ```python
# leah_chocolates = 32
# sister_chocolates = 42
# total_chocolates = leah_chocolates + sister_chocolates
# chocolates_eaten = 35
# chocolates_left = total_chocolates - chocolates_eaten
# answer = chocolates_left
# ```
# ]"""

