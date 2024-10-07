COMMONSENSEQA_FEWSHOT_EXAMPLES_REFLEXION_COT_REFLECT = """Read the following question and then choose the correct answer:

Question: The sanctions against the school were a punishing blow, and they seemed to what the efforts the school had made to change?
Choices: A: ignore, B: enforce, C: authoritarian, D: yell at, E: avoid
Answer: A
Thought: Let's think step by step. The sanctions were a response to efforts, so they must have a direct impact.
Action: Finish[A]
Observation: Generated answer is INCORRECT

Reflection: My reasoning failed because I incorrectly chose "enforce" which does not align with the negative impact implied by "punishing blow". The correct answer should reflect a negation or invalidation of efforts. In the future, I should ensure to consider the context of the impact described.

---

Read the following question and then choose the correct answer:

Question: Sammy wanted to go to where the people were. Where might he go?
Choices: A: race track, B: populated areas, C: the desert, D: apartment, E: roadblock
Answer: B
Thought: Let's think step by step. Sammy wants to be where people are commonly found.
Action: Finish[D]
Observation: Generated answer is INCORRECT

Reflection: My reasoning failed because I chose a specific location (apartment) rather than a broader area where people gather. In the future, I should focus on more general terms that cover multiple possible locations where people are.

---

Read the following question and then choose the correct answer:

Question: To locate a choker not located in a jewelry box or boutique where would you go?
Choices: A: jewelry store, B: neck, C: jewelry box, D: jewelry box, E: boutique
Answer: A
Thought: Let's think step by step. A choker is typically worn as jewelry, so we should look in places associated with jewelry.
Action: Finish[E]
Observation: Generated answer is INCORRECT

Reflection: My reasoning failed because I repeated an answer that was already excluded (boutique). The correct answer should consider a place directly associated with wearing a choker. In the future, I should carefully eliminate options already ruled out in the question.

---

Read the following question and then choose the correct answer:

Question: Google Maps and other highway and street GPS services have replaced what?
Choices: A: united states, B: mexico, C: countryside, D: atlas, E: oceans
Answer: D
Thought: Let's think step by step. GPS services are used for navigation, so they likely replaced traditional navigation aids.
Action: Finish[C]
Observation: Generated answer is INCORRECT

Reflection: My reasoning failed because I chose a geographical area rather than a navigational tool. The correct answer should reflect an outdated navigational aid that GPS services have rendered obsolete. In the future, I should focus on tools or items replaced by technology.

---

Read the following question and then choose the correct answer:

Question: The fox walked from the city into the forest, what was it looking for?
Choices: A: pretty flowers, B: hen house, C: natural habitat, D: storybook, E: dense forest
Answer: C
Thought: Let's think step by step. The fox went to the forest for a reason likely related to its needs or instincts.
Action: Finish[B]
Observation: Generated answer is INCORRECT

Reflection: My reasoning failed because I chose an option (hen house) that is not typically found in a forest. The correct answer should consider the natural behavior and habitat of a fox. In the future, I should ensure to choose answers that align with the natural instincts and habitats of animals."""

REFLEXION_COT_REFLECT_INSTRUCTION_COMMONSENSEQA = """You are an advanced reasoning agent that can improve based on self reflection. You will be given a previous reasoning trial in which you were given a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>] or there is a phrasing discrepancy with your provided answer and the answer key. In a few sentences, diagnose a possible reason for failure or phrasing discrepancy and devise a new, concise, high-level plan that aims to mitigate the same failure. Use complete sentences.

Here are some examples:
{examples}
(END OF EXAMPLES)

Previous trial:
{question}
{scratchpad}

Reflection:"""

REFLEXION_COT_INSTRUCTION_COMMONSENSEQA = """Solve a commonsense question task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task.

Here are some examples:
{examples}
(END OF EXAMPLES)

{reflections}

{question}
{scratchpad}"""

REFLEXION_REACT_INSTRUCTION_COMMONSENSEQA = """Answer a commonsense question with interleaving Thought, Action, Observation steps. Thought can reason about the current question and plan the retrieval steps, and Action can be two types:
(1) Choose[<answer>], which selects the answer to the commonsense question.
(2) Finish[<answer>], which returns the answer to the commonsense question and finishes the task.
You have a maximum of {max_steps} steps.

Here are some examples:
{examples}
(END OF EXAMPLES)

{reflections}

{question}
{scratchpad}"""

REFLEXION_REACT_REFLECT_INSTRUCTION_COMMONSENSEQA = """You are an advanced reasoning agent that can improve based on self reflection. You will be given a previous reasoning trial in which you were given access to a Docstore API environment and a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>], or you used up your set number of reasoning steps. In a few sentences, diagnose a possible reason for failure and devise a new, concise, high-level plan that aims to mitigate the same failure. Use complete sentences.

Here are some examples:
{examples}
(END OF EXAMPLES)

Previous trial:
{question}
{scratchpad}

Reflection:"""

COMMONSENSEQA_FEWSHOT_EXAMPLES_REFLEXION_REACT_REFLECT = """Read the following question and then choose the correct answer:

Question: The sanctions against the school were a punishing blow, and they seemed to what the efforts the school had made to change?
Choices: A: ignore, B: enforce, C: authoritarian, D: yell at, E: avoid
Answer: A
Thought 1: I need to understand the impact of the sanctions on the school's efforts to change.
Action 1: Choose[B]
Observation 1: 
```python
options = ["ignore", "enforce", "authoritarian", "yell at", "avoid"]
answer = options[1]  # enforce
```
Execution Status: Done
Output: answer = enforce
Thought 2: The sanctions seemed to enforce the school's efforts to change.
Action 2: Finish[B]
Observation 2: Generated answer is INCORRECT

Reflection: My reasoning failed because I incorrectly chose "enforce" which does not align with the negative impact implied by "punishing blow". The correct answer should reflect a negation or invalidation of efforts. In the future, I should ensure to consider the context of the impact described.

---

Read the following question and then choose the correct answer:

Question: Sammy wanted to go to where the people were. Where might he go?
Choices: A: race track, B: populated areas, C: the desert, D: apartment, E: roadblock
Answer: B
Thought 1: I need to determine the best option that indicates a place with many people.
Action 1: Choose[D]
Observation 1: 
```python
options = ["race track", "populated areas", "the desert", "apartment", "roadblock"]
answer = options[3]  # apartment
```
Execution Status: Done
Output: answer = apartment
Thought 2: Sammy would go to an apartment where many people live.
Action 2: Finish[D]
Observation 2: Generated answer is INCORRECT

Reflection: My reasoning failed because I chose a specific location (apartment) rather than a broader area where people gather. In the future, I should focus on more general terms that cover multiple possible locations where people are.

---

Read the following question and then choose the correct answer:

Question: To locate a choker not located in a jewelry box or boutique where would you go?
Choices: A: jewelry store, B: neck, C: jewelry box, D: jewelry box, E: boutique
Answer: A
Thought 1: I need to determine the most likely place to find a choker if it's not in a jewelry box or boutique.
Action 1: Choose[E]
Observation 1: 
```python
options = ["jewelry store", "neck", "jewelry box", "jewelry box", "boutique"]
answer = options[4]  # boutique
```
Execution Status: Done
Output: answer = boutique
Thought 2: A choker can be found in a boutique where jewelry is sold.
Action 2: Finish[E]
Observation 2: Generated answer is INCORRECT

Reflection: My reasoning failed because I repeated an answer that was already excluded (boutique). The correct answer should consider a place directly associated with wearing a choker. In the future, I should carefully eliminate options already ruled out in the question.

---

Read the following question and then choose the correct answer:

Question: Google Maps and other highway and street GPS services have replaced what?
Choices: A: united states, B: mexico, C: countryside, D: atlas, E: oceans
Answer: D
Thought 1: I need to determine what traditional item GPS services have replaced.
Action 1: Choose[C]
Observation

 1: 
```python
options = ["united states", "mexico", "countryside", "atlas", "oceans"]
answer = options[2]  # countryside
```
Execution Status: Done
Output: answer = countryside
Thought 2: GPS services replaced the need to navigate through the countryside.
Action 2: Finish[C]
Observation 2: Generated answer is INCORRECT

Reflection: My reasoning failed because I chose a geographical area rather than a navigational tool. The correct answer should reflect an outdated navigational aid that GPS services have rendered obsolete. In the future, I should focus on tools or items replaced by technology.

---

Read the following question and then choose the correct answer:

Question: The fox walked from the city into the forest, what was it looking for?
Choices: A: pretty flowers, B: hen house, C: natural habitat, D: storybook, E: dense forest
Answer: C
Thought 1: I need to determine what a fox would look for in a forest.
Action 1: Choose[B]
Observation 1: 
```python
options = ["pretty flowers.", "hen house", "natural habitat", "storybook", "dense forest"]
answer = options[1]  # hen house
```
Execution Status: Done
Output: answer = hen house
Thought 2: The fox went to the forest to find a hen house.
Action 2: Finish[B]
Observation 2: Generated answer is INCORRECT

Reflection: My reasoning failed because I chose an option (hen house) that is not typically found in a forest. The correct answer should consider the natural behavior and habitat of a fox. In the future, I should ensure to choose answers that align with the natural instincts and habitats of animals."""
