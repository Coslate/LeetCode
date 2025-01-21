#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    nums = [1,1,1,1,1]
    target = 3
    print(f"ans = {Solution().findTargetSumWays(nums, target)}")

    print(f"//Case2:")
    nums = [1]
    target = 1
    print(f"ans = {Solution().findTargetSumWays(nums, target)}")

    print(f"//Case3:")
    nums = [0]
    target = 0
    print(f"ans = {Solution().findTargetSumWays(nums, target)}")



#---------------Execution---------------#
if __name__ == '__main__':
    main()
