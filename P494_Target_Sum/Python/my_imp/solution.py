from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import Counter, deque
import math
import numpy as np
import heapq
import random

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:    
        # Time: O(n*total_sum) | Space: O(n*total_sum)
        # Dynamic Programming
        # Where n is the length of nums, and total_sum = sum(nums)
        # dp[i][j] = the number of comb. to reach target j using first i index in nums.

        total_sum = sum(nums)
        dp = [[0]*(2*total_sum+1) for _ in range(len(nums))] # since we cannot use dp[i][-j] for negative sum value to index, so we shift the whole index from [-total_sum, total_sum] to [0, 2*total_sum].

        # Initializing
        dp[0][nums[0]+total_sum] = 1
        dp[0][-nums[0]+total_sum] += 1

        # Bottom-Up all intermediate sum
        for i in range(1, len(nums)):
            for partial_sum in range(-total_sum, total_sum+1):
                # Continue to increment only when previous sum has contribution.
                if dp[i-1][partial_sum+total_sum] > 0:
                    dp[i][partial_sum+nums[i]+total_sum] += dp[i-1][partial_sum+total_sum]
                    dp[i][partial_sum-nums[i]+total_sum] += dp[i-1][partial_sum+total_sum]

        return 0 if abs(target) > total_sum else dp[len(nums)-1][target+total_sum]

