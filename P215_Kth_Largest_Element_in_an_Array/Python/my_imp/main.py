#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    nums = [3,2,1,5,6,4]
    k = 2
    ans = Solution().findKthLargest(nums, k)
    ans_qs = Solution().findKthLargestQuickSelect(nums, k)
    print(f"ans = {ans}")
    print(f"ans_qs = {ans_qs}")

    print(f"//Case2:")
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    ans = Solution().findKthLargest(nums, k)
    ans_qs = Solution().findKthLargestQuickSelect(nums, k)
    print(f"ans = {ans}")
    print(f"ans_qs = {ans_qs}")



#---------------Execution---------------#
if __name__ == '__main__':
    main()
