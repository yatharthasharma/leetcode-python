from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
  result = set()
  nums.sort()
  for index in range(len(nums)):
    fixed = nums[index]
    p1 = index+1
    p2 = len(nums) - 1
    while p1 < p2:
      if nums[p1] + nums[p2] + fixed == 0:
        result.add((fixed, nums[p1], nums[p2]))
        p1+=1
        p2-=1
      elif nums[p1] + nums[p2] + fixed > 0:
        p2 -= 1
      else:
        p1 += 1
  return list(result)
  
print(
  three_sum([-2,0,1,1,2]))