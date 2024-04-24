from typing import Optional, List
import math

class Solution:
    def findMinPtr(self, nums: List[int]) -> int:
        # Array | Binary Search | Time: O(logn) | Space: O(logn), n is the size of input array
        left_ptr = 0
        right_ptr = len(nums)-1

        if left_ptr == right_ptr:
            return left_ptr

        if nums[left_ptr] <= nums[right_ptr]: #no rotation
            return left_ptr

        while left_ptr < right_ptr:
            mid_ptr = math.ceil((left_ptr + right_ptr)/2) #since need to check mid_ptr-1, we need to round up as the mid_ptr

            if nums[mid_ptr-1] > nums[mid_ptr]: #Find the inflection point
                return mid_ptr
            elif nums[left_ptr] <  nums[mid_ptr]: #Find the inflection point in the right subarray
                left_ptr = mid_ptr
            else: #Find the inflection point in the left subarray
                right_ptr = mid_ptr

        return -1

    def binSearch(self, left_ptr: int, right_ptr: int, nums: List[int], target: int) -> int:
        if left_ptr == right_ptr:
            if nums[left_ptr] == target:
                return left_ptr
            else:
                return -1

        while left_ptr <= right_ptr:
            mid_ptr = (left_ptr + right_ptr)//2

            if target == nums[mid_ptr]:
                return mid_ptr
            elif target > nums[mid_ptr]:
                left_ptr = mid_ptr+1
            else:
                right_ptr = mid_ptr-1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        min_ptr = self.findMinPtr(nums)

        if min_ptr == 0:
            return self.binSearch(0, len(nums)-1, nums, target)
        else:
            if target == nums[0]:
                return 0
            elif target > nums[0]:
                return self.binSearch(0, min_ptr-1, nums, target)
            else:
                return self.binSearch(min_ptr, len(nums)-1, nums, target)

class OptSolution:
    def findMin(self, nums: List[int]) -> int:
        # Array | Binary Search | Time: O(logn) | Space: O(logn), n is the size of input array
        pass

