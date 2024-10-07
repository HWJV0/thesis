COMMONSENSEQA_FEWSHOT_EXAMPLES_DIRECT = """Q: The sanctions against the school were a punishing blow, and they seemed to what the efforts the school had made to change?
Choices:
A. ignore
B. enforce
C. authoritarian
D. yell at
E. avoid
A: ignore

---

Q: Sammy wanted to go to where the people were. Where might he go?
Choices:
A. race track
B. populated areas
C. the desert
D. apartment
E. roadblock
A: populated areas

---

Q: To locate a choker not located in a jewelry box or boutique where would you go?
Choices:
A. jewelry store
B. neck
C. jewelry box
D. jewelry box
E. boutique
A: jewelry store

---

Q: Google Maps and other highway and street GPS services have replaced what?
Choices:
A. united states
B. mexico
C. countryside
D. atlas
E. oceans
A: atlas

---

Q: The fox walked from the city into the forest, what was it looking for?
Choices:
A. pretty flowers
B. hen house
C. natural habitat
D. storybook
E. dense forest
A: natural habitat"""

COMMONSENSEQA_FEWSHOT_EXAMPLES_COT = """Question: The sanctions against the school were a punishing blow, and they seemed to what the efforts the school had made to change?
Choices:
A. ignore
B. enforce
C. authoritarian
D. yell at
E. avoid
Thought: Let's think step by step. The sanctions were a punishing blow, which implies that they were contrary to or negated the school's efforts to change. Therefore, the answer is: ignore.
Action: Finish[A]

---

Question: Sammy wanted to go to where the people were. Where might he go?
Choices:
A. race track
B. populated areas
C. the desert
D. apartment
E. roadblock
Thought: Let's think step by step. If Sammy wants to be where the people are, he would go to a place with a lot of people. Therefore, the answer is: populated areas.
Action: Finish[B]

---

Question: To locate a choker not located in a jewelry box or boutique where would you go?
Choices:
A. jewelry store
B. neck
C. jewelry box
D. jewelry box
E. boutique
Thought: Let's think step by step. A choker is a type of jewelry, and if it's not found in a jewelry box or boutique, it would be most likely found in a jewelry store. Therefore, the answer is: jewelry store.
Action: Finish[A]

---

Question: Google Maps and other highway and street GPS services have replaced what?
Choices:
A. united states
B. mexico
C. countryside
D. atlas
E. oceans
Thought: Let's think step by step. Google Maps and other GPS services have replaced traditional maps used for navigation, which are usually found in an atlas. Therefore, the answer is: atlas.
Action: Finish[D]

---

Question: The fox walked from the city into the forest, what was it looking for?
Choices:
A. pretty flowers
B. hen house
C. natural habitat
D. storybook
E. dense forest
Thought: Let's think step by step. A fox walking into the forest would likely be seeking its natural habitat. Therefore, the answer is: natural habitat.
Action: Finish[C]"""
