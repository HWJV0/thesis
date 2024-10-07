GSMHARD_FEWSHOT_EXAMPLES_AGENT_COT = """Question: Jason had 2000521421.75 lollipops. He gave Denny some lollipops. Now Jason has 1200642521.25 lollipops. How many lollipops did Jason give to Denny? Solve the math question.
Thought: Let's think step by step. Jason initially had 2000521421.75 lollipops. After giving some to Denny, he had 1200642521.25 lollipops left. To find how many he gave to Denny, we subtract the remaining lollipops from the initial amount: 2000521421.75 - 1200642521.25 = 799878900.50. Therefore, Jason gave 799878900.50 lollipops to Denny.
Action: Finish[799878900.50 lollipops]


Question: There are 1564005 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 2215050 trees. How many trees did the grove workers plant today? Solve the math question.
Thought: Let's think step by step. Initially, there were 1564005 trees in the grove. After the workers planted some more, there were 2215050 trees. The number of trees planted is the difference between the final and initial number of trees: 2215050 - 1564005 = 651045. Therefore, the workers planted 651045 trees today.
Action: Finish[651045 trees]


Question: There were 9540930 computers in the server room. 577240 more computers were installed each day, from Monday to Thursday. How many computers are now in the server room? Solve the math question.
Thought: Let's think step by step. Initially, there were 9540930 computers in the server room. From Monday to Thursday, which is 4 days, 577240 computers were installed each day. The total number of computers installed is 577240 * 4 = 2308960. Adding this to the initial 9540930 computers, the total number of computers in the server room is 9540930 + 2308960 = 11849890.
Action: Finish[11849890 computers]


Question: Michael had 58250218 golf balls. On Tuesday, he lost 23405604 golf balls. On Wednesday, he lost 1997112 more. How many golf balls did he have at the end of Wednesday? Solve the math question.
Thought: Let's think step by step. Michael started with 58250218 golf balls. He lost 23405604 golf balls on Tuesday, leaving him with 58250218 - 23405604 = 34844614 golf balls. On Wednesday, he lost 1997112 more, so we subtract 1997112 from 34844614, which gives 34844614 - 1997112 = 32847502. Therefore, he had 32847502 golf balls at the end of Wednesday.
Action: Finish[32847502 golf balls]


Question: If there are 3115697 cars in the parking lot and 1923681 more cars arrive, how many cars are in the parking lot? Solve the math question.
Thought: Let's think step by step. Initially, there are 3115697 cars in the parking lot. When 1923681 more cars arrive, we add the 1923681 cars to the original 3115697 cars, giving us 3115697 + 1923681 = 5039378 cars in total.
Action: Finish[5039378 cars]


Question: Olivia has $23405604.50. She bought five bagels for $3115697.10 each. How much money does she have left? Solve the math question.
Thought: Let's think step by step. Olivia started with $23405604.50. She bought 5 bagels, each costing $3115697.10. The total cost of the bagels is 5 * $3115697.10 = $15578485.50. To find how much money she has left, we subtract the cost of the bagels from her initial amount: $23405604.50 - $15578485.50 = $7827119.0.
Action: Finish[$7827119.0]


Question: Leah had 31997112 chocolates and her sister had 41997112. If they ate 35841028 how many pieces do they have left in total? Solve the math question.
Thought: Let's think step by step. Leah had 31997112 chocolates, and her sister had 41997112 chocolates. Together, they had 31997112 + 41997112 = 73994224 chocolates. They ate 35841028 chocolates, so the number of chocolates they have left is 73994224 - 35841028 = 38153196.
Action: Finish[38153196 pieces of chocolate]"""


GSMHARD_FEWSHOT_EXAMPLES_AGENT_COT_POT = """Question: Jason had 2000521421.75 lollipops. He gave Denny some lollipops. Now Jason has 1200642521.25 lollipops. How many lollipops did Jason give to Denny? Solve the math question.
Thought: Let's think step by step. Jason initially had a certain amount of lollipops. He gave some lollipops to Denny, which reduced his total number of lollipops. Now Jason has a new, smaller amount of lollipops. To find out how many lollipops Jason gave to Denny, we need to subtract the number of lollipops Jason has now from the number of lollipops he originally had. Thus, the formula would be: Lollipops given to Denny = Initial number of lollipops − Current number of lollipops
Action: Finish[
```python
initial_lollipops = 2000521421.75

# Current number of lollipops
current_lollipops = 1200642521.25

# Lollipops given to Denny
lollipops_given = initial_lollipops - current_lollipops

answer = lollipops_given
```
]


Question: There are 1564005 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 2215050 trees. How many trees did the grove workers plant today? Solve the math question.
Thought: Let's think step by step. Initially, there is a certain number of trees in the grove. Grove workers will plant more trees, increasing the total number of trees in the grove. After planting, the total number of trees becomes a new, larger number. To find out how many trees the workers planted, we need to subtract the initial number of trees from the total number of trees after planting.Thus, the formula would be: Trees planted = New total number of trees - Initial number of trees

Action: Finish[
```python
# Initial number of trees in the grove
initial_trees = 1564005

# Total number of trees after planting
new_total_trees = 2215050

# Trees planted
trees_planted = new_total_trees - initial_trees

answer = trees_planted
```
]


Question: There were 9540930 computers in the server room. 577240 more computers were installed each day, from Monday to Thursday. How many computers are now in the server room? Solve the math question.
Thought: Let's think step by step. Initially, there is a certain number of computers in the server room. Each day from Monday to Thursday, a certain number of computers are installed. The total increase in the number of computers is the number of computers installed each day multiplied by the number of days (Monday to Thursday, which is 4 days). To find out how many computers are now in the server room, we need to add this total increase to the initial number of computers. Thus, the formula would be: Total computers now = Initial number of computers + (Number of computers installed each day x 4)

Action: Finish[
```python
# Initial number of computers in the server room
initial_computers = 9540930

# Number of computers installed each day
computers_installed_per_day = 577240

# Number of days from Monday to Thursday
days = 4

# Total computers installed over the 4 days
total_installed = computers_installed_per_day * days

# Total computers now in the server room
total_computers = initial_computers + total_installed

answer = total_computers
```
]


Question: Michael had 58250218 golf balls. On Tuesday, he lost 23405604 golf balls. On Wednesday, he lost 1997112 more. How many golf balls did he have at the end of Wednesday? Solve the math question.
Thought: Let's think step by step. Michael initially had a certain number of golf balls. On Tuesday, he lost a specific number of golf balls, which reduced his total count. On Wednesday, he lost some more golf balls. To find out how many golf balls he had at the end of Wednesday, we need to subtract both the number of golf balls lost on Tuesday and Wednesday from the initial number of golf balls. Thus, the formula would be: Golf balls at the end of Wednesday = Initial number of golf balls - (Golf balls lost on Tuesday + Golf balls lost on Wednesday)

Action: Finish[
```python
# Initial number of golf balls
initial_golf_balls = 58250218

# Golf balls lost on Tuesday
golf_balls_lost_tuesday = 23405604

# Golf balls lost on Wednesday
golf_balls_lost_wednesday = 1997112

# Total golf balls lost
total_lost = golf_balls_lost_tuesday + golf_balls_lost_wednesday

# Golf balls at the end of Wednesday
remaining_golf_balls = initial_golf_balls - total_lost

answer = remaining_golf_balls
```
]


Question: If there are 3115697 cars in the parking lot and 1923681 more cars arrive, how many cars are in the parking lot? Solve the math question.
Thought: Let's think step by step. Initially, there are a certain number of cars in the parking lot. After that, more cars arrive, increasing the total number of cars. To find out how many cars are in the parking lot now, we need to add the number of cars that arrived to the initial number of cars. Thus, the formula would be: Total cars in the parking lot = Initial number of cars + Number of cars that arrived
Action: Finish[
```python
# Initial number of cars in the parking lot
initial_cars = 3115697

# Number of cars that arrived
cars_arrived = 1923681

# Total cars in the parking lot
total_cars = initial_cars + cars_arrived

answer = total_cars
```
]


Question: Olivia has $23405604.50. She bought five bagels for $3115697.10 each. How much money does she have left? Solve the math question.
Thought: Let's think step by step. Olivia initially has a certain amount of money. She buys five bagels, each costing a certain amount. To find out how much money she has left, we need to subtract the total cost of the five bagels from her initial amount of money. The total cost of the bagels will be the price of one bagel multiplied by five. Thus, the formula would be: Money left = Initial amount of money - (Price of one bagel × Number of bagels)

Action: Finish[
```python
# Initial amount of money Olivia has
initial_money = 23405604.50

# Price of one bagel
price_per_bagel = 3115697.10

# Number of bagels bought
number_of_bagels = 5

# Total cost of the bagels
total_cost = price_per_bagel * number_of_bagels

# Money left after purchase
money_left = initial_money - total_cost

answer = money_left
```
]


Question: Leah had 31997112 chocolates and her sister had 41997112. If they ate 35841028 how many pieces do they have left in total? Solve the math question.
Thought: Let's think step by step. Leah and her sister initially have a certain number of chocolates combined. They ate a certain number of chocolates, reducing the total amount they have. To find out how many chocolates they have left in total, we need to subtract the number of chocolates they ate from the combined initial amount of chocolates. Thus, the formula would be: Chocolates left = (Leah's chocolates + Sister's chocolates) - Chocolates eaten
Action: Finish[
```python
# Leah's chocolates
leahs_chocolates = 31997112

# Sister's chocolates
sisters_chocolates = 41997112

# Chocolates eaten
chocolates_eaten = 35841028

# Total chocolates left
total_chocolates_left = (leahs_chocolates + sisters_chocolates) - chocolates_eaten

total_chocolates_left

answer = total_chocolates_left
```
]"""