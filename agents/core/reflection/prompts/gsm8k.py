#############
# REFLEXION #
#############

GSM8K_FEWSHOT_REFLEXION_EXAMPLES_NEGATIVE = """Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
Thought: Let's think step by step. Jason had 20 lollipops initially and now he has 12 lollipops. So, he must have given 20 + 12 = 32 lollipops to Denny.
Action: Finish[32 lollipops]
Observation: The generated answer is INCORRECT.
Reflection: My reasoning failed because I incorrectly added the initial and remaining lollipops instead of subtracting the remaining from the initial to find out how many were given away. In the future, I should ensure to carefully review the mathematical operations required to solve the problem accurately.


Question: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
Thought: Let's think step by step. There were initially 15 trees and after planting, there are 21 trees. So, the number of trees planted is 15 - 21 = -6.
Action: Finish[-6 trees]
Observation: The generated answer is INCORRECT.
Reflection: My reasoning failed because I subtracted the final number of trees from the initial number of trees instead of subtracting the initial number from the final number. In the future, I should ensure to correctly apply the operations needed to find the difference.


Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
Thought: Let's think step by step. Shawn had 5 toys initially, and he got 2 toys from his mom and 2 toys from his dad. So, the total number of toys he has now is 5 + 2 = 7.
Action: Finish[7 toys]
Observation: The generated answer is INCORRECT.
Reflection: My reasoning failed because I only added the toys from his mom and forgot to include the toys from his dad. In the future, I should ensure to account for all given quantities in the problem to arrive at the correct solution.


Question: There were nine computers in the server room. Five more computers were installed each day, from Monday to Thursday. How many computers are now in the server room?
Thought: Let's think step by step. Initially, there were 9 computers. Five more computers were added each day from Monday to Thursday, which is 4 days. So, the total number of computers added is 5 + 4 = 9. Therefore, the total number of computers now is 9 + 9 = 18.
Action: Finish[18 computers]
Observation: The generated answer is INCORRECT.
Reflection: My reasoning failed because I incorrectly added the number of computers per day to the number of days instead of multiplying them. In the future, I should ensure to use the correct operations to calculate the total number of items added.


Question: Michael had 58 golf balls. On Tuesday, he lost 23 golf balls. On Wednesday, he lost 2 more. How many golf balls did he have at the end of Wednesday?
Thought: Let's think step by step. Michael initially had 58 golf balls. He lost 23 golf balls on Tuesday and 2 more on Wednesday. So, the total number of golf balls lost is 23 + 2 = 25. Therefore, the number of golf balls he has left is 58 + 25 = 83.
Action: Finish[83 golf balls]
Observation: The generated answer is INCORRECT.
Reflection: My reasoning failed because I incorrectly added the total number of golf balls lost to the initial number of golf balls instead of subtracting it. In the future, I should ensure to use the correct operation (subtraction) to find the remaining number of items."""


GSM8K_FEWSHOT_REFLEXION_EXAMPLES_MIXED = """Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
Thought: Let's think step by step. Jason had 20 lollipops initially and now he has 12 lollipops. So, he must have given 20 + 12 = 32 lollipops to Denny.
Action: Finish[32 lollipops]
Observation: The generated answer is INCORRECT.
Reflection: My reasoning failed because I incorrectly added the initial and remaining lollipops instead of subtracting the remaining from the initial to find out how many were given away. In the future, I should ensure to carefully review the mathematical operations required to solve the problem accurately.


Question: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
Thought: Let's think step by step. There were initially 15 trees and after planting, there are 21 trees. So, the number of trees planted is 21 - 15 = 6.
Action: Finish[6 trees]
Observation: The generated answer is CORRECT.
Reflection: My reasoning is correct because I identified the initial number of trees and the total number of trees after planting. By subtracting the initial number of trees from the total number, I accurately calculate the number of trees planted.


Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
Thought: Let's think step by step. Shawn had 5 toys initially, and he got 2 toys from his mom and 2 toys from his dad. So, the total number of toys he has now is 5 + 2 = 7.
Action: Finish[7 toys]
Observation: The generated answer is INCORRECT
Reflection: My reasoning failed because I only added the toys from his mom and forgot to include the toys from his dad. In the future, I should ensure to account for all given quantities in the problem to arrive at the correct solution.


Question: There were nine computers in the server room. Five more computers were installed each day, from Monday to Thursday. How many computers are now in the server room?
Thought: Let's think step by step. Initially, there were 9 computers. Five more computers were added each day from Monday to Thursday, which is 4 days. So, the total number of computers added is 5 * 4 = 20. Therefore, the total number of computers now is 9 + 20 = 29.
Action: Finish[29 computers]
Observation: The generated answer is CORRECT
Reflection: My reasoning is correct because I accurately multiply the number of computers added each day by the number of days to find the total number of additional computers. By adding this result to the initial number of computers, I calculated the correct total.


Question: Michael had 58 golf balls. On Tuesday, he lost 23 golf balls. On Wednesday, he lost 2 more. How many golf balls did he have at the end of Wednesday?
Thought: Let's think step by step. Michael initially had 58 golf balls. He lost 23 golf balls on Tuesday and 2 more on Wednesday. So, the total number of golf balls lost is 23 + 2 = 25. Therefore, the number of golf balls he has left is 58 + 25 = 83.
Action: Finish[83 golf balls]
Observation: The generated answer is INCORRECT
Reflection: My reasoning failed because I incorrectly added the total number of golf balls lost to the initial number of golf balls instead of subtracting it. In the future, I should ensure to use the correct operation (subtraction) to find the remaining number of items."""


##################
# SELFREFLECTION #
################## 

GSM8K_FEWSHOT_SELFREFLECTION_EXAMPLES_NEGATIVE = """Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
Thought: Let's think step by step. Jason had 20 lollipops initially and now he has 12 lollipops. So, he must have given 20 + 12 = 32 lollipops to Denny.
Action: Finish[32 lollipops]
Observation: The generated answer is 32 lollipops.
Reflection: My reasoning failed because I incorrectly added the initial and remaining lollipops instead of subtracting the remaining from the initial to find out how many were given away. In the future, I should ensure to carefully review the mathematical operations required to solve the problem accurately.


Question: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
Thought: Let's think step by step. There were initially 15 trees and after planting, there are 21 trees. So, the number of trees planted is 15 - 21 = -6.
Action: Finish[-6 trees]
Observation: The generated answer is -6 trees.
Reflection: My reasoning failed because I subtracted the final number of trees from the initial number of trees instead of subtracting the initial number from the final number. In the future, I should ensure to correctly apply the operations needed to find the difference.


Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
Thought: Let's think step by step. Shawn had 5 toys initially, and he got 2 toys from his mom and 2 toys from his dad. So, the total number of toys he has now is 5 + 2 = 7.
Action: Finish[7 toys]
Observation: The generated answer is 7 toys.
Reflection: My reasoning failed because I only added the toys from his mom and forgot to include the toys from his dad. In the future, I should ensure to account for all given quantities in the problem to arrive at the correct solution.


Question: There were nine computers in the server room. Five more computers were installed each day, from Monday to Thursday. How many computers are now in the server room?
Thought: Let's think step by step. Initially, there were 9 computers. Five more computers were added each day from Monday to Thursday, which is 4 days. So, the total number of computers added is 5 + 4 = 9. Therefore, the total number of computers now is 9 + 9 = 18.
Action: Finish[18 computers]
Observation: The generated answer is 18 computers.
Reflection: My reasoning failed because I incorrectly added the number of computers per day to the number of days instead of multiplying them. In the future, I should ensure to use the correct operations to calculate the total number of items added.


Question: Michael had 58 golf balls. On Tuesday, he lost 23 golf balls. On Wednesday, he lost 2 more. How many golf balls did he have at the end of Wednesday?
Thought: Let's think step by step. Michael initially had 58 golf balls. He lost 23 golf balls on Tuesday and 2 more on Wednesday. So, the total number of golf balls lost is 23 + 2 = 25. Therefore, the number of golf balls he has left is 58 + 25 = 83.
Action: Finish[83 golf balls]
Observation: The generated answer is 83 golf balls.
Reflection: My reasoning failed because I incorrectly added the total number of golf balls lost to the initial number of golf balls instead of subtracting it. In the future, I should ensure to use the correct operation (subtraction) to find the remaining number of items."""


GSM8K_FEWSHOT_SELFREFLECTION_EXAMPLES_MIXED = """Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
Thought: Let's think step by step. Jason had 20 lollipops initially and now he has 12 lollipops. So, he must have given 20 + 12 = 32 lollipops to Denny.
Action: Finish[32 lollipops]
Observation: The generated answer is 32 lollipops.
Reflection: My reasoning failed because I incorrectly added the initial and remaining lollipops instead of subtracting the remaining from the initial to find out how many were given away. In the future, I should ensure to carefully review the mathematical operations required to solve the problem accurately.


Question: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
Thought: Let's think step by step. There were initially 15 trees and after planting, there are 21 trees. So, the number of trees planted is 21 - 15 = 6.
Action: Finish[6 trees]
Observation: The generated answer is 6 trees.
Reflection: My reasoning is correct because I identified the initial number of trees and the total number of trees after planting. By subtracting the initial number of trees from the total number, I accurately calculate the number of trees planted.


Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
Thought: Let's think step by step. Shawn had 5 toys initially, and he got 2 toys from his mom and 2 toys from his dad. So, the total number of toys he has now is 5 + 2 = 7.
Action: Finish[7 toys]
Observation: The generated answer is 7 toys.
Reflection: My reasoning failed because I only added the toys from his mom and forgot to include the toys from his dad. In the future, I should ensure to account for all given quantities in the problem to arrive at the correct solution.


Question: There were nine computers in the server room. Five more computers were installed each day, from Monday to Thursday. How many computers are now in the server room?
Thought: Let's think step by step. Initially, there were 9 computers. Five more computers were added each day from Monday to Thursday, which is 4 days. So, the total number of computers added is 5 * 4 = 20. Therefore, the total number of computers now is 9 + 20 = 29.
Action: Finish[29 computers]
Observation: The generated answer is 29 computers.
Reflection: My reasoning is correct because I accurately multiply the number of computers added each day by the number of days to find the total number of additional computers. By adding this result to the initial number of computers, I calculated the correct total.


Question: Michael had 58 golf balls. On Tuesday, he lost 23 golf balls. On Wednesday, he lost 2 more. How many golf balls did he have at the end of Wednesday?
Thought: Let's think step by step. Michael initially had 58 golf balls. He lost 23 golf balls on Tuesday and 2 more on Wednesday. So, the total number of golf balls lost is 23 + 2 = 25. Therefore, the number of golf balls he has left is 58 + 25 = 83.
Action: Finish[83 golf balls]
Observation: The generated answer is 83 golf balls.
Reflection: My reasoning failed because I incorrectly added the total number of golf balls lost to the initial number of golf balls instead of subtracting it. In the future, I should ensure to use the correct operation (subtraction) to find the remaining number of items."""


# GSM8K_FEWSHOT_EXAMPLES_SELFREFLECTION_COT_POT_REFLECT_NEGATIVE_EXAMPLES = """Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
# Thought: Let's think step by step. Jason had 20 lollipops initially and now he has 12 lollipops. So, he must have given 20 + 12 = 32 lollipops to Denny.
# Action: Finish[
# ```python
# jason_lollipops_initial = 20
# jason_lollipops_after = 12
# denny_lollipops = jason_lollipops_initial + jason_lollipops_after
# answer = denny_lollipops
# ```
# ]
# Observation: The generated answer is 32

# Reflection: My reasoning failed because I incorrectly added the initial and remaining lollipops instead of subtracting the remaining from the initial to find out how many were given away. In the future, I should ensure to carefully review the mathematical operations required to solve the problem accurately.

# ---

# Question: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
# Thought: Let's think step by step. There were initially 15 trees and after planting, there are 21 trees. So, the number of trees planted is 15 - 21 = -6.
# Action: Finish[
# ```python
# trees_initial = 15
# trees_after = 21
# trees_added = trees_initial - trees_after
# answer = trees_added
# ```
# ]
# Observation: The generated answer is -6

# Reflection: My reasoning failed because I subtracted the final number of trees from the initial number of trees instead of subtracting the initial number from the final number. In the future, I should ensure to correctly apply the operations needed to find the difference.

# ---

# Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
# Thought: Let's think step by step. Shawn had 5 toys initially, and he got 2 toys from his mom and 2 toys from his dad. So, the total number of toys he has now is 5 + 2 = 7.
# Action: Finish[
# ```python
# toys_initial = 5
# mom_toys = 2
# dad_toys = 2
# total_toys = toys_initial + mom_toys
# answer = total_toys
# ```
# ]
# Observation: The generated answer is 7

# Reflection: My reasoning failed because I only added the toys from his mom and forgot to include the toys from his dad. In the future, I should ensure to account for all given quantities in the problem to arrive at the correct solution.

# ---

# Question: There were nine computers in the server room. Five more computers were installed each day, from Monday to Thursday. How many computers are now in the server room?
# Thought: Let's think step by step. Initially, there were 9 computers. Five more computers were added each day from Monday to Thursday, which is 4 days. So, the total number of computers added is 5 + 4 = 9. Therefore, the total number of computers now is 9 + 9 = 18.
# Action: Finish[
# ```python
# computers_initial = 9
# computers_per_day = 5
# num_days = 4  # 4 days between Monday and Thursday
# computers_added = computers_per_day + num_days
# computers_total = computers_initial + computers_added
# answer = computers_total
# ```
# ]
# Observation: The generated answer is 18

# Reflection: My reasoning failed because I incorrectly added the number of computers per day to the number of days instead of multiplying them. In the future, I should ensure to use the correct operations to calculate the total number of items added.

# ---

# Question: Michael had 58 golf balls. On Tuesday, he lost 23 golf balls. On Wednesday, he lost 2 more. How many golf balls did he have at the end of Wednesday?
# Thought: Let's think step by step. Michael initially had 58 golf balls. He lost 23 golf balls on Tuesday and 2 more on Wednesday. So, the total number of golf balls lost is 23 + 2 = 25. Therefore, the number of golf balls he has left is 58 + 25 = 83.
# Action: Finish[
# ```python
# golf_balls_initial = 58
# golf_balls_lost_tuesday = 23
# golf_balls_lost_wednesday = 2
# golf_balls_lost_total = golf_balls_lost_tuesday + golf_balls_lost_wednesday
# golf_balls_left = golf_balls_initial + golf_balls_lost_total
# answer = golf_balls_left
# ```
# ]
# Observation: The generated answer is 83

# Reflection: My reasoning failed because I incorrectly added the total number of golf balls lost to the initial number of golf balls instead of subtracting it. In the future, I should ensure to use the correct operation (subtraction) to find the remaining number of items."""


# GSM8K_FEWSHOT_EXAMPLES_REFLEXION_COT_POT_REFLECT_NEGATIVE_EXAMPLES = """Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
# Thought: Let's think step by step. Jason had 20 lollipops initially and now he has 12 lollipops. So, he must have given 20 + 12 = 32 lollipops to Denny.
# Action: Finish[
# ```python
# jason_lollipops_initial = 20
# jason_lollipops_after = 12
# denny_lollipops = jason_lollipops_initial + jason_lollipops_after
# answer = denny_lollipops
# ```
# ]
# Observation: The generated answer is INCORRECT

# Reflection: My reasoning failed because I incorrectly added the initial and remaining lollipops instead of subtracting the remaining from the initial to find out how many were given away. In the future, I should ensure to carefully review the mathematical operations required to solve the problem accurately.

# ---

# Question: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
# Thought: Let's think step by step. There were initially 15 trees and after planting, there are 21 trees. So, the number of trees planted is 15 - 21 = -6.
# Action: Finish[
# ```python
# trees_initial = 15
# trees_after = 21
# trees_added = trees_initial - trees_after
# answer = trees_added
# ```
# ]
# Observation: The generated answer is INCORRECT

# Reflection: My reasoning failed because I subtracted the final number of trees from the initial number of trees instead of subtracting the initial number from the final number. In the future, I should ensure to correctly apply the operations needed to find the difference.

# ---

# Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
# Thought: Let's think step by step. Shawn had 5 toys initially, and he got 2 toys from his mom and 2 toys from his dad. So, the total number of toys he has now is 5 + 2 = 7.
# Action: Finish[
# ```python
# toys_initial = 5
# mom_toys = 2
# dad_toys = 2
# total_toys = toys_initial + mom_toys
# answer = total_toys
# ```
# ]
# Observation: The generated answer is INCORRECT

# Reflection: My reasoning failed because I only added the toys from his mom and forgot to include the toys from his dad. In the future, I should ensure to account for all given quantities in the problem to arrive at the correct solution.

# ---

# Question: There were nine computers in the server room. Five more computers were installed each day, from Monday to Thursday. How many computers are now in the server room?
# Thought: Let's think step by step. Initially, there were 9 computers. Five more computers were added each day from Monday to Thursday, which is 4 days. So, the total number of computers added is 5 + 4 = 9. Therefore, the total number of computers now is 9 + 9 = 18.
# Action: Finish[
# ```python
# computers_initial = 9
# computers_per_day = 5
# num_days = 4  # 4 days between Monday and Thursday
# computers_added = computers_per_day + num_days
# computers_total = computers_initial + computers_added
# answer = computers_total
# ```
# ]
# Observation: The generated answer is INCORRECT

# Reflection: My reasoning failed because I incorrectly added the number of computers per day to the number of days instead of multiplying them. In the future, I should ensure to use the correct operations to calculate the total number of items added.

# ---

# Question: Michael had 58 golf balls. On Tuesday, he lost 23 golf balls. On Wednesday, he lost 2 more. How many golf balls did he have at the end of Wednesday?
# Thought: Let's think step by step. Michael initially had 58 golf balls. He lost 23 golf balls on Tuesday and 2 more on Wednesday. So, the total number of golf balls lost is 23 + 2 = 25. Therefore, the number of golf balls he has left is 58 + 25 = 83.
# Action: Finish[
# ```python
# golf_balls_initial = 58
# golf_balls_lost_tuesday = 23
# golf_balls_lost_wednesday = 2
# golf_balls_lost_total = golf_balls_lost_tuesday + golf_balls_lost_wednesday
# golf_balls_left = golf_balls_initial + golf_balls_lost_total
# answer = golf_balls_left
# ```
# ]
# Observation: The generated answer is INCORRECT

# Reflection: My reasoning failed because I incorrectly added the total number of golf balls lost to the initial number of golf balls instead of subtracting it. In the future, I should ensure to use the correct operation (subtraction) to find the remaining number of items."""


# GSM8K_FEWSHOT_EXAMPLES_SELFREFLECTION_COT_POT_REFLECT_NEGATIVE_EXAMPLES = """Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
# Thought: Let's think step by step. Jason had 20 lollipops initially and now he has 12 lollipops. So, he must have given 20 + 12 = 32 lollipops to Denny.
# Action: Finish[
# ```python
# jason_lollipops_initial = 20
# jason_lollipops_after = 12
# denny_lollipops = jason_lollipops_initial + jason_lollipops_after
# answer = denny_lollipops
# ```
# ]
# Observation: The generated answer is 32

# Reflection: My reasoning failed because I incorrectly added the initial and remaining lollipops instead of subtracting the remaining from the initial to find out how many were given away. In the future, I should ensure to carefully review the mathematical operations required to solve the problem accurately.

# ---

# Question: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
# Thought: Let's think step by step. There were initially 15 trees and after planting, there are 21 trees. So, the number of trees planted is 15 - 21 = -6.
# Action: Finish[
# ```python
# trees_initial = 15
# trees_after = 21
# trees_added = trees_initial - trees_after
# answer = trees_added
# ```
# ]
# Observation: The generated answer is -6

# Reflection: My reasoning failed because I subtracted the final number of trees from the initial number of trees instead of subtracting the initial number from the final number. In the future, I should ensure to correctly apply the operations needed to find the difference.

# ---

# Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
# Thought: Let's think step by step. Shawn had 5 toys initially, and he got 2 toys from his mom and 2 toys from his dad. So, the total number of toys he has now is 5 + 2 = 7.
# Action: Finish[
# ```python
# toys_initial = 5
# mom_toys = 2
# dad_toys = 2
# total_toys = toys_initial + mom_toys
# answer = total_toys
# ```
# ]
# Observation: The generated answer is 7

# Reflection: My reasoning failed because I only added the toys from his mom and forgot to include the toys from his dad. In the future, I should ensure to account for all given quantities in the problem to arrive at the correct solution.

# ---

# Question: There were nine computers in the server room. Five more computers were installed each day, from Monday to Thursday. How many computers are now in the server room?
# Thought: Let's think step by step. Initially, there were 9 computers. Five more computers were added each day from Monday to Thursday, which is 4 days. So, the total number of computers added is 5 + 4 = 9. Therefore, the total number of computers now is 9 + 9 = 18.
# Action: Finish[
# ```python
# computers_initial = 9
# computers_per_day = 5
# num_days = 4  # 4 days between Monday and Thursday
# computers_added = computers_per_day + num_days
# computers_total = computers_initial + computers_added
# answer = computers_total
# ```
# ]
# Observation: The generated answer is 18

# Reflection: My reasoning failed because I incorrectly added the number of computers per day to the number of days instead of multiplying them. In the future, I should ensure to use the correct operations to calculate the total number of items added.

# ---

# Question: Michael had 58 golf balls. On Tuesday, he lost 23 golf balls. On Wednesday, he lost 2 more. How many golf balls did he have at the end of Wednesday?
# Thought: Let's think step by step. Michael initially had 58 golf balls. He lost 23 golf balls on Tuesday and 2 more on Wednesday. So, the total number of golf balls lost is 23 + 2 = 25. Therefore, the number of golf balls he has left is 58 + 25 = 83.
# Action: Finish[
# ```python
# golf_balls_initial = 58
# golf_balls_lost_tuesday = 23
# golf_balls_lost_wednesday = 2
# golf_balls_lost_total = golf_balls_lost_tuesday + golf_balls_lost_wednesday
# golf_balls_left = golf_balls_initial + golf_balls_lost_total
# answer = golf_balls_left
# ```
# ]
# Observation: The generated answer is 83

# Reflection: My reasoning failed because I incorrectly added the total number of golf balls lost to the initial number of golf balls instead of subtracting it. In the future, I should ensure to use the correct operation (subtraction) to find the remaining number of items."""


# GSM8K_FEWSHOT_EXAMPLES_SELFREFLECTION_COT_POT_REFLECT_MIXED_EXAMPLES = """Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
# Thought: Let's think step by step. Jason had 20 lollipops initially and now he has 12 lollipops. So, he must have given 20 + 12 = 32 lollipops to Denny.
# Action: Finish[
# ```python
# jason_lollipops_initial = 20
# jason_lollipops_after = 12
# denny_lollipops = jason_lollipops_initial + jason_lollipops_after
# answer = denny_lollipops
# ```
# ]
# Observation: The generated answer is 32

# Reflection: My reasoning failed because I incorrectly added the initial and remaining lollipops instead of subtracting the remaining from the initial to find out how many were given away. In the future, I should ensure to carefully review the mathematical operations required to solve the problem accurately.

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
# Observation: The generated answer is 6

# Reflection: My reasoning is correct because I identified the initial number of trees and the total number of trees after planting. By subtracting the initial number of trees from the total number, I accurately calculate the number of trees planted.

# ---

# Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
# Thought: Let's think step by step. Shawn had 5 toys initially, and he got 2 toys from his mom and 2 toys from his dad. So, the total number of toys he has now is 5 + 2 = 7.
# Action: Finish[
# ```python
# toys_initial = 5
# mom_toys = 2
# dad_toys = 2
# total_toys = toys_initial + mom_toys
# answer = total_toys
# ```
# ]
# Observation: The generated answer is 7

# Reflection: My reasoning failed because I only added the toys from his mom and forgot to include the toys from his dad. In the future, I should ensure to account for all given quantities in the problem to arrive at the correct solution.

# ---

# Question: There were nine computers in the server room. Five more computers were installed each day, from Monday to Thursday. How many computers are now in the server room?
# Thought: Let's think step by step. Initially, there were 9 computers. Five more computers were added each day from Monday to Thursday, which is 4 days. So, the total number of computers added is 5 * 4 = 20. Therefore, the total number of computers now is 9 + 20 = 29.
# Action: Finish[
# ```python
# computers_initial = 9
# computers_per_day = 5
# num_days = 4  # 4 days between monday and thursday
# computers_added = computers_per_day * num_days
# computers_total = computers_initial + computers_added
# answer = computers_total
# ```
# ]
# Observation: The generated answer is 29

# Reflection: My reasoning is correct because I accurately multiply the number of computers added each day by the number of days to find the total number of additional computers. By adding this result to the initial number of computers, I calculated the correct total.

# ---

# Question: Michael had 58 golf balls. On Tuesday, he lost 23 golf balls. On Wednesday, he lost 2 more. How many golf balls did he have at the end of Wednesday?
# Thought: Let's think step by step. Michael initially had 58 golf balls. He lost 23 golf balls on Tuesday and 2 more on Wednesday. So, the total number of golf balls lost is 23 + 2 = 25. Therefore, the number of golf balls he has left is 58 + 25 = 83.
# Action: Finish[
# ```python
# golf_balls_initial = 58
# golf_balls_lost_tuesday = 23
# golf_balls_lost_wednesday = 2
# golf_balls_lost_total = golf_balls_lost_tuesday + golf_balls_lost_wednesday
# golf_balls_left = golf_balls_initial + golf_balls_lost_total
# answer = golf_balls_left
# ```
# ]
# Observation: The generated answer is 83

# Reflection: My reasoning failed because I incorrectly added the total number of golf balls lost to the initial number of golf balls instead of subtracting it. In the future, I should ensure to use the correct operation (subtraction) to find the remaining number of items."""

# GSM8K_FEWSHOT_EXAMPLES_REFLEXION_COT_POT_REFLECT_MIXED_EXAMPLES = """Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
# Thought: Let's think step by step. Jason had 20 lollipops initially and now he has 12 lollipops. So, he must have given 20 + 12 = 32 lollipops to Denny.
# Action: Finish[
# ```python
# jason_lollipops_initial = 20
# jason_lollipops_after = 12
# denny_lollipops = jason_lollipops_initial + jason_lollipops_after
# answer = denny_lollipops
# ```
# ]
# Observation: The generated answer is INCORRECT

# Reflection: My reasoning failed because I incorrectly added the initial and remaining lollipops instead of subtracting the remaining from the initial to find out how many were given away. In the future, I should ensure to carefully review the mathematical operations required to solve the problem accurately.

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
# Observation: The generated answer is CORRECT

# Reflection: My reasoning is correct because I identified the initial number of trees and the total number of trees after planting. By subtracting the initial number of trees from the total number, I accurately calculate the number of trees planted.

# ---

# Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
# Thought: Let's think step by step. Shawn had 5 toys initially, and he got 2 toys from his mom and 2 toys from his dad. So, the total number of toys he has now is 5 + 2 = 7.
# Action: Finish[
# ```python
# toys_initial = 5
# mom_toys = 2
# dad_toys = 2
# total_toys = toys_initial + mom_toys
# answer = total_toys
# ```
# ]
# Observation: The generated answer is INCORRECT

# Reflection: My reasoning failed because I only added the toys from his mom and forgot to include the toys from his dad. In the future, I should ensure to account for all given quantities in the problem to arrive at the correct solution.

# ---

# Question: There were nine computers in the server room. Five more computers were installed each day, from Monday to Thursday. How many computers are now in the server room?
# Thought: Let's think step by step. Initially, there were 9 computers. Five more computers were added each day from Monday to Thursday, which is 4 days. So, the total number of computers added is 5 * 4 = 20. Therefore, the total number of computers now is 9 + 20 = 29.
# Action: Finish[
# ```python
# computers_initial = 9
# computers_per_day = 5
# num_days = 4  # 4 days between monday and thursday
# computers_added = computers_per_day * num_days
# computers_total = computers_initial + computers_added
# answer = computers_total
# ```
# ]
# Observation: The generated answer is CORRECT

# Reflection: My reasoning is correct because I accurately multiply the number of computers added each day by the number of days to find the total number of additional computers. By adding this result to the initial number of computers, I calculated the correct total.

# ---

# Question: Michael had 58 golf balls. On Tuesday, he lost 23 golf balls. On Wednesday, he lost 2 more. How many golf balls did he have at the end of Wednesday?
# Thought: Let's think step by step. Michael initially had 58 golf balls. He lost 23 golf balls on Tuesday and 2 more on Wednesday. So, the total number of golf balls lost is 23 + 2 = 25. Therefore, the number of golf balls he has left is 58 + 25 = 83.
# Action: Finish[
# ```python
# golf_balls_initial = 58
# golf_balls_lost_tuesday = 23
# golf_balls_lost_wednesday = 2
# golf_balls_lost_total = golf_balls_lost_tuesday + golf_balls_lost_wednesday
# golf_balls_left = golf_balls_initial + golf_balls_lost_total
# answer = golf_balls_left
# ```
# ]
# Observation: The generated answer is INCORRECT

# Reflection: My reasoning failed because I incorrectly added the total number of golf balls lost to the initial number of golf balls instead of subtracting it. In the future, I should ensure to use the correct operation (subtraction) to find the remaining number of items."""

# REFLEXION_REFLECT_INSTRUCTION_GSM8K = """You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>] or there is a phrasing discrepancy with your provided answer and the answer key. In a few sentences, diagnose a possible reason for failure or phrasing discrepancy and devise a new, concise, high level plan that aims to mitigate the same failure. Use complete sentences.

# Here are some examples:
# {examples}
# (END OF EXAMPLES)

# Previous trial:
# Question: {question}{scratchpad}

# Reflection:"""

# REFLEXION_REFLECT_INSTRUCTION_GSM8K_ZEROSHOT = """You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>] or there is a phrasing discrepancy with your provided answer and the answer key. In a few sentences, diagnose a possible reason for failure or phrasing discrepancy and devise a new, concise, high level plan that aims to mitigate the same failure. Use complete sentences.

# Previous trial:
# Question: {question}{scratchpad}

# Reflection:"""

# SELFREFLECTION_REFLECT_INSTRUCTION_GSM8K_NEGATIVE_PROMPT = """You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given a question to answer. You could have been unsuccessful in answering the question either because you guessed the wrong answer with Finish[answer] or there is a phrasing discrepancy with your provided answer and the answer key. In a few sentences, diagnose a possible reason for failure or phrasing discrepancy and devise a new, concise, high level plan that aims to mitigate the same failure. Use complete sentences.

# Solve the following task by having a Thought to reason through the problem, then provide the final answer as executable Python code in the Finish section.

# Here are some examples:
# {examples}
# (END OF EXAMPLES)

# Previous trial:
# Question: {question}{scratchpad}

# Reflection:"""

# SELFREFLECTION_REFLECT_INSTRUCTION_GSM8K_NEGATIVE_PROMPT_ZEROSHOT = """You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given a question to answer. You could have been unsuccessful in answering the question either because you guessed the wrong answer with Finish[answer] or there is a phrasing discrepancy with your provided answer and the answer key. In a few sentences, diagnose a possible reason for failure or phrasing discrepancy and devise a new, concise, high level plan that aims to mitigate the same failure. Use complete sentences.

# Previous trial:
# Question: {question}{scratchpad}

# Reflection:"""

# SELFREFLECTION_REFLECT_INSTRUCTION_GSM8K_CRITICAL_PROMPT = """You are an advanced reasoning agent that can improve based on self reflection. You will be given a previous reasoning trial in which you were given a question to answer. Critically evaluate if your answer with Finish[answer] is correct. Identify any areas that might benefit from correction and develop a concise, high-level plan to correct your approach if needed. Use complete sentences to describe your findings and strategy."

# Here are some examples:
# {examples}
# (END OF EXAMPLES)

# Previous trial:
# Question: {question}{scratchpad}

# Reflection:"""

# SELFREFLECTION_REFLECT_INSTRUCTION_GSM8K_CRITICAL_PROMPT_ZEROSHOT = """You are an advanced reasoning agent that can improve based on self reflection. You will be given a previous reasoning trial in which you were given a question to answer. Critically evaluate if your answer with Finish[answer] is correct. Identify any areas that might benefit from correction and develop a concise, high-level plan to correct your approach if needed. Use complete sentences to describe your findings and strategy."

# Previous trial:
# Question: {question}{scratchpad}

# Reflection:"""

# REFLEXION_COT_POT_INSTRUCTION_GSM8K = """Solve a math question task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task.

# Here are some examples:
# {examples}
# (END OF EXAMPLES)

# {reflections}

# Question: {question}{scratchpad}"""

# REFLEXION_COT_POT_INSTRUCTION_GSM8K_ZEROSHOT = """Solve a math question task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[```python code```] returns the code to answer the math question and finishes the task, saving the answer as the `answer` variable.

# Here is the format:
# Thought: Let's think step by step.
# Action: Finish[```python code```]
# Observation: Answer is <answer>
# (END OF FORMAT)

# {reflections}

# Question: {question}{scratchpad}"""


# GSM8K_FEWSHOT_EXAMPLES_SELFREFLECTION_REACT_REFLECT = """Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
# Thought 1: First, I need to find out how many lollipops Jason gave to Denny.
# Action 1: Calculate[
# ```python
# jason_lollipops_initial = 20
# jason_lollipops_after = 12
# answer = jason_lollipops_after + jason_lollipops_initial
# ```
# ]
# Observation 1: 
# ```python
# jason_lollipops_initial = 20
# jason_lollipops_after = 12
# answer = jason_lollipops_after + jason_lollipops_initial
# ```
# Execution Status: Done
# Output: answer = 32
# Thought 2: The answer seems too high, but I will proceed with this calculation.
# Action 2: Finish[
# ```python
# answer = 32
# ```
# ]
# Observation 2: The generated answer is 32

# Reflection: My reasoning failed because I added the remaining lollipops to the initial count instead of subtracting the remaining from the initial to find out how many were given away. In the future, I should ensure to carefully review the mathematical operations required to solve the problem accurately. The correct operation should have been subtraction, not addition.

# ---

# Question: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
# Thought 1: I need to determine how many trees were planted.
# Action 1: Calculate[
# ```python
# trees_initial = 15
# trees_after = 21
# answer = trees_initial - trees_after
# ```
# ]
# Observation 1: 
# ```python
# trees_initial = 15
# trees_after = 21
# answer = trees_initial - trees_after
# ```
# Execution Status: Done
# Output: answer = -6
# Thought 2: The answer should be positive because trees are being added, not removed. However, I will proceed with the subtraction result.
# Action 2: Finish[
# ```python
# answer = -6
# ```
# ]
# Observation 2: The generated answer is -6

# Reflection: My reasoning failed because I subtracted the final number of trees from the initial number instead of the correct operation, which is subtracting the initial number of trees from the final number. In the future, I should ensure to carefully review the mathematical operations required to solve the problem accurately. The correct answer should be obtained by reversing the subtraction to reflect the addition of trees.

# ---

# Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
# Thought 1: I need to calculate the total number of toys Shawn has after receiving gifts from his parents.
# Action 1: Calculate[
# ```python
# toys_initial = 5
# toys_received_mom = 2
# toys_received_dad = 2
# answer = toys_initial + toys_received_mom + toys_received_dad
# ```
# ]
# Observation 1: 
# ```python
# toys_initial = 5
# toys_received_mom = 2
# toys_received_dad = 2
# answer = toys_initial + toys_received_mom + toys_received_dad
# ```
# Execution Status: Done
# Output: answer = 9
# Thought 2: I realize that I calculated the total toys received correctly. However, I will double-check by using another method.
# Action 2: Calculate[
# ```python
# toys_initial = 5
# toys_received = 2 * 3
# answer = toys_initial + toys_received
# ```
# ]
# Observation 2: 
# ```python
# toys_initial = 5
# toys_received = 2 * 3
# answer = toys_initial + toys_received
# ```
# Execution Status: Done
# Output: answer = 11
# Thought 3: According to my second calculation, Shawn has 11 toys now. I need to confirm the total number of toys.
# Action 3: Finish[
# ```python
# answer = 11
# ```
# ]
# Observation 3: The generated answer is 11

# Reflection: My reasoning failed because I mistakenly multiplied the number of toys received instead of adding the correct amounts. Initially, I calculated correctly by adding the 2 toys received from mom and 2 toys received from dad to the initial 5 toys. However, my second method was incorrect as I wrongly multiplied the toys received. In the future, I should ensure to stick with the correct arithmetic operations and verify my calculations accurately. The correct answer should be 9 toys.

# ---

# Question: There were nine computers in the server room. Five more computers were installed each day, from Monday to Thursday. How many computers are now in the server room?
# Thought 1: I need to calculate the total number of computers installed from Monday to Thursday.
# Action 1: Calculate[
# ```python
# computers_initial = 9
# computers_per_day = 5
# num_days = 4  # 4 days between Monday and Thursday
# computers_added = computers_per_day * num_days
# answer = computers_initial + computers_added
# ```
# ]
# Observation 1: 
# ```python
# computers_initial = 9
# computers_per_day = 5
# num_days = 4  # 4 days between Monday and Thursday
# computers_added = computers_per_day * num_days
# answer = computers_initial + computers_added
# ```
# Execution Status: Done
# Output: answer = 29
# Thought 2: The total number of computers seems high. Let me verify by recalculating step-by-step.
# Action 2: Calculate[
# ```python
# computers_per_day = 5
# num_days = 4
# computers_added = computers_per_day + num_days
# answer = computers_initial + computers_added
# ```
# ]
# Observation 2: 
# ```python
# computers_per_day = 5
# num_days = 4
# computers_added = computers_per_day + num_days
# answer = computers_initial + computers_added
# ```
# Execution Status: Done
# Output: answer = 18
# Thought 3: The recalculated total is 18 computers.
# Action 3: Finish[
# ```python
# answer = 18
# ```
# ]
# Observation 3: The generated answer is 18

# Reflection: My reasoning failed because I incorrectly recalculated the total number of computers added by summing the computers per day and the number of days instead of multiplying them. The correct approach was in my initial calculation, where I correctly multiplied the number of computers installed per day by the number of days and added that to the initial number of computers. In the future, I should ensure to carefully review my calculations and verify the arithmetic operations used. The correct answer should have been 29 computers.

# ---

# Question: Michael had 58 golf balls. On Tuesday, he lost 23 golf balls. On Wednesday, he lost 2 more. How many golf balls did he have at the end of Wednesday?
# Thought 1: I need to find out how many golf balls Michael has after losing some on Tuesday and Wednesday.
# Action 1: Calculate[
# ```python
# golf_balls_initial = 58
# golf_balls_lost_tuesday = 23
# golf_balls_lost_wednesday = 2
# answer = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday
# ```
# ]
# Observation 1: 
# ```python
# golf_balls_initial = 58
# golf_balls_lost_tuesday = 23
# golf_balls_lost_wednesday = 2
# answer = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday
# ```
# Execution Status: Done
# Output: answer = 33
# Thought 2: The answer seems low. I should verify my calculations by adding the losses instead of subtracting directly.
# Action 2: Calculate[
# ```python
# total_golf_balls_lost = golf_balls_lost_tuesday + golf_balls_lost_wednesday
# answer = golf_balls_initial + total_golf_balls_lost
# ```
# ]
# Observation 2: 
# ```python
# total_golf_balls_lost = golf_balls_lost_tuesday + golf_balls_lost_wednesday
# answer = golf_balls_initial + total_golf_balls_lost
# ```
# Execution Status: Done
# Output: answer = 83
# Thought 3: The recalculated total is 83 golf balls.
# Action 3: Finish[
# ```python
# answer = 83
# ```
# ]
# Observation 3: The generated answer is 83

# Reflection: My reasoning failed because I incorrectly added the golf balls lost to the initial number of golf balls instead of subtracting them. Initially, I correctly subtracted the losses from the total, but I doubted my correct method and made a mistake in the verification step. In the future, I should ensure to trust the initial correct arithmetic operations and avoid unnecessary recalculations that lead to errors. The correct answer should have been 33 golf balls."""
