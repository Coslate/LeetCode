#! /usr/bin/env python3

from solution import *

def main():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"nums1 = {nums1}, m = {m}")
    print(f"nums2 = {nums2}, n = {n}")

    print(f"//------Merged-------//")
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    print(f"nums1 = {nums1}")
    print(f"")
    print(f"")

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"nums1 = {nums1}, m = {m}")
    print(f"nums2 = {nums2}, n = {n}")

    print(f"//------Merged-------//")
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    print(f"nums1 = {nums1}")
    print(f"")
    print(f"")

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"nums1 = {nums1}, m = {m}")
    print(f"nums2 = {nums2}, n = {n}")

    print(f"//------Merged-------//")
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    print(f"nums1 = {nums1}")
    print(f"")
    print(f"")

    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    print(f"//Case4:")
    print(f"//------Original-------//")
    print(f"nums1 = {nums1}, m = {m}")
    print(f"nums2 = {nums2}, n = {n}")

    print(f"//------Merged-------//")
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    print(f"nums1 = {nums1}")
    print(f"")
    print(f"")



#---------------Execution---------------#
if __name__ == '__main__':
    main()
