from typing import List


def car_fleet(target: int, position: List[int], speed: List[int]) -> int:
  merged_list = zip(position, speed)
  stack = []
  for x, y in sorted(merged_list)[::-1]:
    time = (target - x) / y
    if stack:
      if stack[-1] < time:
        stack.append(time)
    else:
      stack.append(time)
  return len(stack)


print(car_fleet(12, [10,8,0,5,3], [2,4,1,1,3]))