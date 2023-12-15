from typing import Optional, List

class Solution:
    def atMost(self, nums: List[int], k:int) -> int:
        #return the number of at most k odd number occured subarray
        i = 0
        nums_of_subarray = 0

        for j in range(len(nums)):
            k -= ((nums[j])%2)
            while k < 0:
                k += (nums[i]%2)
                i += 1
            nums_of_subarray += j-i+1

        return nums_of_subarray

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Sliding Window | Time: O(n) | Space: O(1)
        return self.atMost(nums, k) - self.atMost(nums, k-1)


class OptSolution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Sliding Window | Time: O(n) | Space: O(1)
        # Same as above
        pass


