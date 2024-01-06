from typing import List


def search(nums: List[int], target: int) -> int:
  p1 = 0
  p2 = len(nums) - 1
  while p1 < p2:
    median = (p1 + p2) // 2
    median_number = nums[median]
    if target == median_number:
      return median
    elif target > median_number:
      p1 = median + 1
    else:
      p2 = median - 1
  return p1 if target == nums[p1] else -1

print(search([2,5], 0))