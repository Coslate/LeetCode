from typing import Optional, List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # linear merge | Time: O(m+n) | Space: O(m+n)

        ptr1 = 0
        ptr2 = 0
        result_arr = []
        for index, element in enumerate(nums1):
            if ptr1 == m:
                result_arr.append(nums2[ptr2])
                ptr2 += 1
            elif ptr2 == n:
                result_arr.append(nums1[ptr1])
                ptr1 += 1
            else:
                if nums2[ptr2] < nums1[ptr1]:
                    #swap(), euqls to nums1[ptr1], nums2[ptr2] = nums2[ptr2], nums1[ptr1]
                    result_arr.append(nums2[ptr2])
                    ptr2 += 1
                else:
                    result_arr.append(nums1[ptr1])
                    ptr1 += 1

        #affect the original nums1
        nums1[:] = result_arr[:]

class OptSolution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # linear merge | Time: O(m+n) | Space: O(1)

        ptr1 = m-1
        ptr2 = n-1
        k    = m+n-1

        while ptr2 >= 0:
            if ptr1 >=0 and nums1[ptr1] > nums2[ptr2]:
                nums1[k] = nums1[ptr1]
                k    -= 1
                ptr1 -= 1
            else:
                nums1[k] = nums2[ptr2]
                k    -= 1
                ptr2 -= 1

