from typing import Optional, List
import collections

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Sliding Window | Time: O(n) | Space: O(1)
        i = 0
        ans = -1
        num_size = len(nums)

        for j in range(num_size):
            k -= 1-nums[j]

            while k < 0:
                ans = max(ans, j-i)
                k += 1-nums[i]
                i += 1

            if j == num_size-1:
                ans = max(ans, j-i+1)

        return ans

class OptSolution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Sliding Window | Time: O(n) | Space: O(1)
        i = 0
        num_size = len(nums)

        for j in range(num_size):
            k -= 1-nums[j]

            if k < 0:
                k += 1-nums[i]
                i += 1
        return j-i+1


