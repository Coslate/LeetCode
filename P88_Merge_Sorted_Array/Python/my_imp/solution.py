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

