from typing import Optional, List
import math
from numpy.linalg import matrix_power
import numpy as np

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Dynamic Programming | Time: O(n^2) | Space: O(n), n is the length of nums.
        dp = [1]*len(nums)
        max_result = -1
        for i in range(len(nums)):
            for j in range(0, i):
                dp[i] = max(dp[j]+1, dp[i]) if nums[j] < nums[i] else dp[i]
            max_result = max(max_result, dp[i])

        return max_result

class OptSolution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        res = -1

        while left <= right:
            mid = (left+right)//2
            if target > nums[mid]:
                left = mid+1
                res = mid+1
            elif target < nums[mid]:
                right = mid-1
                res = mid
            else:
                res = mid
                break
        return res

    def lengthOfLIS(self, nums: List[int]) -> int:
        # Binary Search | Time: O(nlogn) | Space: O(n), n is the length of nums
        constructed_optsol = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > constructed_optsol[-1]:
                constructed_optsol.append(nums[i])
            elif nums[i] < constructed_optsol[-1]:
                inserted_pos = self.binarySearch(constructed_optsol, nums[i])
                constructed_optsol[inserted_pos] = nums[i]

        return len(constructed_optsol)


