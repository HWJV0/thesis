NPTRIPPLANNING_FEWSHOT_EXAMPLES_AGENT_COT = """Question: You plan to visit 3 European cities for 7 days in total. You only take direct flights to commute between cities. You want to spend 4 days in Berlin. You would like to visit Venice for 3 days. You are going to attend a wedding in Venice between day 5 and day 7. You want to spend 2 days in Tallinn.

Here are the cities that have direct flights:
Berlin and Venice, Tallinn and Berlin.

Find a trip plan of visiting the cities for 7 days by taking direct flights to commute between them.

Thought: Let's think step by step. Since there are direct flights between Berlin and Venice as well as between Tallinn and Berlin, it makes sense to plan the trip around these routes. You want to attend a wedding in Venice from day 5 to day 7, so Venice should be your final stop. Since you need to visit Berlin for 4 days, it’s ideal to place it in the middle of the trip after spending 2 days in Tallinn. This plan ensures you attend the wedding on time and cover all cities with direct flight routes.
Action: Finish[Here is the trip plan for visiting the 3 European cities for 7 days:

**Day 1-2:** Arriving in Tallinn and visit Tallinn for 2 days.
**Day 2:** Fly from Tallinn to Berlin.
**Day 2-5:** Visit Berlin for 4 days.
**Day 5:** Fly from Berlin to Venice.
**Day 5-7:** Visit Venice for 3 days.] 

Question: You plan to visit 3 European cities for 14 days in total. You only take direct flights to commute between cities. You plan to stay in London for 4 days. You plan to stay in Bucharest for 5 days. You want to meet a friend in Bucharest between day 10 and day 14. You would like to visit Reykjavik for 7 days.

Here are the cities that have direct flights:
London and Bucharest, Reykjavik and London.

Find a trip plan of visiting the cities for 14 days by taking direct flights to commute between them.

Thought: Let's think step by step. You want to stay in Reykjavik for 7 days, and there are direct flights between Reykjavik and London. Since you want to meet a friend in Bucharest from day 10 to day 14, Bucharest should be the final stop. This leaves London in the middle of the trip for 4 days. This order of cities ensures you can visit all locations using direct flights and meet your friend at the planned time.
Action: Finish[Here is the trip plan for visiting the 3 European cities for 14 days:

**Day 1-7:** Arriving in Reykjavik and visit Reykjavik for 7 days.
**Day 7:** Fly from Reykjavik to London.
**Day 7-10:** Visit London for 4 days.
**Day 10:** Fly from London to Bucharest.
**Day 10-14:** Visit Bucharest for 5 days.]


Question: You plan to visit 3 European cities for 12 days in total. You only take direct flights to commute between cities. You want to spend 4 days in Seville. You plan to stay in Valencia for 5 days. You have to attend a workshop in Valencia between day 8 and day 12. You plan to stay in Manchester for 5 days.

Here are the cities that have direct flights:
Manchester and Seville, Seville and Valencia.

Find a trip plan of visiting the cities for 12 days by taking direct flights to commute between them.

Thought: Let's think step by step. Since Manchester and Seville have direct flights, and you want to spend 5 days in Manchester, it makes sense to start the trip there. After visiting Manchester, you can fly to Seville for 4 days. As you have a workshop in Valencia from day 8 to day 12, Valencia should be the last destination. This ensures you follow the schedule while taking direct flights.
Action: Finish[Here is the trip plan for visiting the 3 European cities for 12 days:

**Day 1-5:** Arriving in Manchester and visit Manchester for 5 days.
**Day 5:** Fly from Manchester to Seville.
**Day 5-8:** Visit Seville for 4 days.
**Day 8:** Fly from Seville to Valencia.
**Day 8-12:** Visit Valencia for 5 days.]


Question: You plan to visit 3 European cities for 8 days in total. You only take direct flights to commute between cities. You plan to stay in Istanbul for 2 days. You want to spend 3 days in Venice. You have to attend a workshop in Venice between day 1 and day 3. You would like to visit Valencia for 5 days.

Here are the cities that have direct flights:
Venice and Istanbul, Istanbul and Valencia.

Find a trip plan of visiting the cities for 8 days by taking direct flights to commute between them.

Thought: Let's think step by step. You need to attend a workshop in Venice from day 1 to day 3, so Venice must be your first stop. After spending 3 days in Venice, you can fly to Istanbul for 2 days. Since there is a direct flight from Istanbul to Valencia, you can then spend the remaining 5 days in Valencia, ensuring all locations are visited in the desired order using direct flights.
Action: Finish[Here is the trip plan for visiting the 3 European cities for 8 days:

**Day 1-3:** Arriving in Venice and visit Venice for 3 days.
**Day 3:** Fly from Venice to Istanbul.
**Day 3-4:** Visit Istanbul for 2 days.
**Day 4:** Fly from Istanbul to Valencia.
**Day 4-8:** Visit Valencia for 5 days.]


Question: You plan to visit 3 European cities for 11 days in total. You only take direct flights to commute between cities. You want to spend 2 days in Porto. You want to spend 4 days in Oslo. You would like to visit Split for 7 days. You plan to visit relatives in Split between day 5 and day 11.

Here are the cities that have direct flights:
Porto and Oslo, Oslo and Split.

Find a trip plan of visiting the cities for 11 days by taking direct flights to commute between them.

Thought: Let's think step by step. Since there are direct flights from Porto to Oslo, it’s best to start the trip in Porto and spend 2 days there. After that, fly to Oslo for 4 days. Since you plan to visit relatives in Split from day 5 to day 11, Split should be your final destination. This plan ensures you follow the schedule and use only direct flights.
Action: Finish[Here is the trip plan for visiting the 3 European cities for 11 days:

**Day 1-2:** Arriving in Porto and visit Porto for 2 days.
**Day 2:** Fly from Porto to Oslo.
**Day 2-5:** Visit Oslo for 4 days.
**Day 5:** Fly from Oslo to Split.
**Day 5-11:** Visit Split for 7 days.]"""