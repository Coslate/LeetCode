from typing import Optional, List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Sliding Window | Time: O(n) | Space: O(1)
        nums_size = len(nums)
        ans_num = nums_size
        got_once = False
        j = 0

        for i in range(nums_size):
            target -= nums[i]

            while(target <=0 ):
                got_once = True
                ans_num = min(ans_num, i-j+1)
                target += nums[j]
                j += 1

        return ans_num if got_once else 0

class OptSolution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Sliding Window | Time: O(n) | Space: O(1)
        # Same as above
        pass


