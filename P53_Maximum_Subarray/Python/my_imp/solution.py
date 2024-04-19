from typing import Optional, List

class Solution:
    def maxSubArrayRangeSearch(self, left_idx: int, right_idx: int, nums: List[int]) -> int:
        if left_idx > right_idx:
            return float('-inf')

        mid_idx = (left_idx + right_idx)//2

        #Check each possible left-subarray sum value.
        cur_sum = 0
        left_sum_max = 0 #if sum of left has maximum of negative value, then left part has no need to add in. mid-point only is the maximum subarray.
        for idx in range(mid_idx-1, left_idx-1, -1):
            cur_sum += nums[idx]
            left_sum_max = max(left_sum_max, cur_sum)

        #Check each possible right-subarray sum value.
        cur_sum = 0
        right_sum_max = 0 #if sum of right has maximum of negative value, then right part has no need to add in. mid-point only is the maximum subarray.
        for idx in range(mid_idx+1, right_idx+1):
            cur_sum += nums[idx]
            right_sum_max = max(right_sum_max, cur_sum)

        combined_sum_mid = nums[mid_idx] + left_sum_max + right_sum_max

        #Recursively left and right part searching.
        left_possible_sum_max = self.maxSubArrayRangeSearch(left_idx, mid_idx-1, nums)
        right_possible_sum_max = self.maxSubArrayRangeSearch(mid_idx+1, right_idx, nums)

        result = max(combined_sum_mid, left_possible_sum_max, right_possible_sum_max)
        return result

    def maxSubArray(self, nums: List[int]) -> int:
        # Array | Divida and Conquer | Time: O(nlogn) | Space: O(logn), n is the size of input array
        return self.maxSubArrayRangeSearch(0, len(nums)-1, nums)

class OptSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Array | Dynamic Programming, Kadane's Algorithm | Time: O(n) | Space: O(1), n is the size of input array
        start_array_sum = nums[0]
        max_subarray    = nums[0]

        for i in range(1, len(nums)):
            start_array_sum = max(nums[i], nums[i]+start_array_sum)
            max_subarray    = max(max_subarray, start_array_sum)


        return max_subarray
