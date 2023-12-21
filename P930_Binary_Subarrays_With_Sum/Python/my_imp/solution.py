from typing import Optional, List
import collections

class Solution:
    def atMost(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        num_size = len(nums)
        i = 0
        ans = 0
        for j in range(num_size):
            k   -= nums[j]
            while k < 0:
                k += nums[i]
                i += 1
            ans += (j-i+1)
        return ans

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Sliding Window | Time: O(n) | Space: O(1)
        return self.atMost(nums, goal) - self.atMost(nums, goal-1)


class OptSolution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Sliding Window | Time: O(n) | Space: O(1)
        # Same as above
        pass


