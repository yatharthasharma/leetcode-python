import math
from typing import List


def min_eating_speed(piles: List[int], h: int) -> int:
  p1 = 1
  p2 = max(piles)
  overall_min_eating_speed = p2
  while(p1 <= p2):
    eating_speed_per_hour = (p1+p2) // 2
    hours_by_eating_speed = 0
    valid_speed = True
    for item in piles:
      hours_by_eating_speed += math.ceil(item / eating_speed_per_hour)
      if hours_by_eating_speed > h:
        p1 = eating_speed_per_hour + 1
        valid_speed = False
        break
    if valid_speed is True:
      if eating_speed_per_hour < overall_min_eating_speed:
        overall_min_eating_speed = eating_speed_per_hour
        p2 = overall_min_eating_speed - 1
      else:
        p1 = eating_speed_per_hour + 1
  return overall_min_eating_speed


print(min_eating_speed([3,6,7,11], 8))