#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    nums = [1,3,4,2,2]
    ans = Solution().findDuplicate(nums)
    print(f"ans = {ans}")

    print(f"//Case2:")
    nums = [3,1,3,4,2]
    ans = Solution().findDuplicate(nums)
    print(f"ans = {ans}")

    print(f"//Case3:")
    nums = [3,3,3,3,3]
    ans = Solution().findDuplicate(nums)
    print(f"ans = {ans}")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
