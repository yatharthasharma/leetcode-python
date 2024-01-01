from typing import List


def max_area(height: List[int]) -> int:
  current_max = 0
  p1 = 0
  p2 = len(height) - 1
  while p1 < p2:
    length = p2 - p1
    width = min(height[p2], height[p1])
    current_max = max(length * width, current_max)
    if height[p2] > height[p1]:
      p1+=1
    else:
      p2-=1
  return current_max
