from typing import List

class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        forward_product = [1]
        backward_product = [1] * len(nums)
        for index, num in enumerate(nums):
            if index == 0:
                continue
            forward_product.append(forward_product[index - 1] * nums[index - 1])
        for index in reversed(range(len(nums) - 1)):
            backward_product[index] = backward_product[index + 1] * nums[index+1]
        result = []
        for index, num in enumerate(forward_product):
            result.append(num * backward_product[index])
        return result