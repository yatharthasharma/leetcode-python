from typing import List


class Solution:
    # change method name to containsDuplicate when submitting on Leetcode
    def contains_duplicate(self, nums: List[int]) -> bool:
        existing_values = set()
        for num in nums:
          if num in existing_values:
           return True
          else:
           existing_values.add(num)
        return False
            
