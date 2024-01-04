from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
  temperature_index = []
  indices = []
  result = [0] * len(temperatures)
  for index, temp in enumerate(temperatures):
    while len(temperature_index) > 0 and temp > temperature_index[-1]:
      index_to_populate = indices.pop()
      result[index_to_populate] = index - index_to_populate
      temperature_index.pop()
    temperature_index.append(temp)
    indices.append(index)
  return result

daily_temperatures([73,74,75,71,69,72,76,73])