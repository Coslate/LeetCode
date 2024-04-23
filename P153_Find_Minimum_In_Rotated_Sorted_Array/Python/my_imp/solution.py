from typing import Optional, List
import math

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Array | Binary Search | Time: O(logn) | Space: O(logn), n is the size of input array
        left_ptr = 0
        right_ptr = len(nums)-1

        if left_ptr == right_ptr:
            return nums[left_ptr]

        if nums[left_ptr] <= nums[right_ptr]: #no rotation
            return nums[left_ptr]

        while left_ptr < right_ptr:
            mid_ptr = math.ceil((left_ptr + right_ptr)/2) #since need to check mid_ptr-1, we need to round up as the mid_ptr

            if nums[mid_ptr-1] > nums[mid_ptr]: #Find the inflection point
                return nums[mid_ptr]
            elif nums[left_ptr] <  nums[mid_ptr]: #Find the inflection point in the right subarray
                left_ptr = mid_ptr
            else: #Find the inflection point in the left subarray
                right_ptr = mid_ptr

class OptSolution:
    def findMin(self, nums: List[int]) -> int:
        # Array | Binary Search | Time: O(logn) | Space: O(logn), n is the size of input array
        pass

