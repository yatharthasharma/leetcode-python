from typing import List


class Solution:
    # change method name to twoSum when submitting on Leetcode
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        nums_and_index = {};
        for index, num in enumerate(nums):
            number_for_target_total = target - num
            if number_for_target_total in nums_and_index:
                return [index, nums_and_index.get(number_for_target_total)]
            else:
                nums_and_index.update({num: index})