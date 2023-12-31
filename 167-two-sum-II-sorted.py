from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
  p1 = 0
  p2 = len(numbers) - 1
  while p1 < p2:
    sum_of_numbers = numbers[p1] + numbers[p2]
    if sum_of_numbers == target:
      return [p1+1, p2+1]
    elif target < sum_of_numbers:
      p2-=1
    else:
      p1+=1
  return []

print(two_sum([2,7,11,15], 9))