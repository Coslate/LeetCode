from typing import Optional, List
import math

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Bit Operation | Time: O(n) | Space: O(1), n is the input length of
        # array
        mem_one = [0]*10000
        for i in range(len(nums)):
            mem_one[nums[i]] = 1
        for i in range(len(nums)+1):
            if mem_one[i] == 0:
                return i
        return -1

class OptSolution:
    def missingNumber(self, nums: List[int]) -> int:
        # Bit Operation | Gauss' Formula | Time: O(n) | Space: O(1), n is the input length of
        # array
        num_tot = len(nums)
        # expected_sum = 0+1+2+3+...+len(nums)
        expected_sum = ((num_tot+1)*num_tot)//2
        # actual_sum = sum(nums)
        actual_sum = sum(nums)

        return expected_sum-actual_sum
