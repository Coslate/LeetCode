from typing import Optional, List

class Solution:
    def maxSubArrayRangeSearch(self, left_idx: int, right_idx: int, nums: List[int]) -> int:
        if left_idx > right_idx:
            return float('-inf')

        mid_idx = (left_idx + right_idx)//2

        #Check each possible left-subarray sum value.
        cur_sum = 1
        left_pos_max = 1 #if sum of left has maximum of negative value, then left part has no need to add in. mid-point only is the maximum subarray.
        left_neg_max = 1
        for idx in range(mid_idx-1, left_idx-1, -1):
            cur_sum *= nums[idx]
            left_pos_max = max(left_pos_max, cur_sum)
            left_neg_max = min(left_neg_max, cur_sum)

        #Check each possible right-subarray sum value.
        cur_sum = 1
        right_pos_max = 1 #if sum of right has maximum of negative value, then right part has no need to add in. mid-point only is the maximum subarray.
        right_neg_max = 1
        for idx in range(mid_idx+1, right_idx+1):
            cur_sum *= nums[idx]
            right_pos_max = max(right_pos_max, cur_sum)
            right_neg_max = min(right_neg_max, cur_sum)

        if nums[mid_idx] > 0:
            combined_sum_mid = max(nums[mid_idx] * left_pos_max * right_pos_max, nums[mid_idx] * left_neg_max * right_neg_max)
        else:
            combined_sum_mid = max(nums[mid_idx] * left_pos_max * right_neg_max, nums[mid_idx] * left_neg_max * right_pos_max)

        #Recursively left and right part searching.
        left_possible_sum_max = self.maxSubArrayRangeSearch(left_idx, mid_idx-1, nums)
        right_possible_sum_max = self.maxSubArrayRangeSearch(mid_idx+1, right_idx, nums)

        result = max(combined_sum_mid, left_possible_sum_max, right_possible_sum_max)
        return result

    def maxProduct(self, nums: List[int]) -> int:
        # Array | Divida and Conquer | Time: O(nlogn) | Space: O(logn), n is the size of input array
        return self.maxSubArrayRangeSearch(0, len(nums)-1, nums)

class OptSolution:
    def maxProduct(self, nums: List[int]) -> int:
        # Array | Dynamic Programming | Time: O(n) | Space: O(1), n is the size of input array
        min_so_far  = nums[0]
        max_so_far  = nums[0]
        result      = nums[0]

        for i in range(1, len(nums)):
            now_max = max(nums[i], max(max_so_far*nums[i], min_so_far*nums[i]))
            min_so_far = min(nums[i], min(max_so_far*nums[i], min_so_far*nums[i]))
            max_so_far = now_max

            result = max(result, max_so_far)

        return result
