# Copyright 2024 Google LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Eval Script for Trip Planning."""

import json
import re
from typing import Any

from absl import app
from absl import flags


class NPTripPlanningSolution:
  """Class to encapsulate all the parameters required for a Trip Planning solution.

    Attributes:
      cities (str): The cities in the plan in the format of "city1*city2*city3".
      durations (str): The durations of the stay in each city in the format of "1*2*3".
      golden_plan (str): The golden plan in the format of [(city1, stay_days), (city2, stay_days), ...].
  """

  def __init__(self, cities: str, durations: str, golden_plan: list):
    self.cities = cities
    self.durations = durations
    self.golden_plan = golden_plan

  def to_dict(self):
    """
    Converts the instance attributes to a dictionary.
    """

    return {
        'cities': self.cities,
        'durations': self.durations,
        'golden_plan': self.golden_plan,
    }


def parse_response(response: str):
  """Parse the response.

  Returns a parsed plan in a list of (city, stay_days) tuples.

  Args:
    response: Raw response from the model.

  Returns:
    Structured plan after parsing.
  """
  pattern_visit = r'\d+-\d+'
  pattern_flight = r'.*Day (\d+).*from (\w+) to (\w+)'
  pattern_days = r'European cities for (\d+) days'

  days, flights, flight_days = [], [], []
  total_days = None
  for piece in response.split('\n'):
    days_match = re.findall(pattern_days, piece)
    if days_match:
      total_days = int(days_match[0])

    visit_match = re.findall(pattern_visit, piece)
    if visit_match:
      days.append(visit_match[0])
      end_day = int(visit_match[0].split('-')[1])
      # Reach the end of the plan, stop to avoid parsing alternative plans.
      if end_day == total_days:
        break
    flight_match = re.findall(pattern_flight, piece)
    if flight_match:
      flights.append(flight_match[0])

  visit_cities, parsed_plan = [], []
  for flight_day, begin_city, end_city in flights:
    flight_days.append(int(flight_day))
    if not visit_cities:
      visit_cities.append(begin_city)
      visit_cities.append(end_city)
    else:
      visit_cities.append(end_city)

  if not days or not flights or not visit_cities:
    return []
  last_day = int(days[-1].split('-')[1])
  flight_days = [1] + flight_days + [last_day]
  for i, visit_city in enumerate(visit_cities):
    city_stay = flight_days[i + 1] - flight_days[i] + 1
    parsed_plan.append((visit_city, city_stay))

  return parsed_plan


def compute_example_score(cities: str, durations: str, parsed_plan: list[Any]):
  """Compute the exact-match accuracy.

  Compute the example-level exact_match score (0/1) given the parsed plan
  and the ground truth in the format of durations and cities.

  Args:
    cities: The cities in the plan in the format of "city1*city2*city3".
    durations: The durations of the stay in each city in the format of
      "1*2*3".
    parsed_plan: The parsed plan from the response.

  Returns:
    Exact-match accuracy of 0 (mismatched) or 1 (matched).
  """

  stays = [x for x in cities.split('*') if x]
  days = [int(x) for x in durations.split('*') if x]
  num_stays = min(len(stays), len(parsed_plan))
  num_match = 0
  for i in range(num_stays):
    if stays[i] == parsed_plan[i][0] and days[i] == parsed_plan[i][1]:
      num_match += 1
    else:
      break
  hard_score = 0.0 if num_match / len(stays) < 1.0 else 1.0
  return hard_score


def compute_score(
    cities: list[str], durations: list[str], responses: list[str]
):
  """Compute the sample-level exact-match accuracy.

  Args:
    cities: List of cities in the plan in the format of "city1*city2*city3".
    durations: List of durations of the stay in each city in the format of
      "1*2*3".
    responses: The raw responses from the model.

  Returns:
    Exact-match score at the sample level.
  """
  parsed_plans = [parse_response(response) for response in responses]
  hard_scores = [
      compute_example_score(city, duration, parsed_plan)
      for city, duration, parsed_plan in zip(cities, durations, parsed_plans)
  ]
  hard_acc = sum(hard_scores) / len(hard_scores)
  return hard_acc


def tp_is_correct(query, key: NPTripPlanningSolution) -> bool:
    """
    Checks if the predicted plan matches the golden plan based on individual parameters.
    Args:
        query (str): The predicted plan.
        ke (str): The golden plan.
    Returns: 
        bool: True if the predicted plan is correct, False otherwise.
    """

    parsed_pred_plan = parse_response(query)
    score = compute_example_score(key.cities, key.durations, parsed_pred_plan)

    return score == 1.0


# def main(_):
#   with open(_DATA_PATH.value) as f:
#     data = json.load(f)

#   cities, durations, responses = [], [], []
#   sample_count = 0
#   for _, item in data.items():
#     cities.append(item['cities'])
#     durations.append(item['durations'])
#     responses.append(item['pred_5shot_pro'])
#     sample_count += 1

#   hard_acc = compute_score(cities, durations, responses)
#   print(f'EM Accuracy of {sample_count} samples: {hard_acc}')
