#! /usr/bin/env python3

from solution import Solution

def main():
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]

    ans = sol.threeSum(nums)
    print(f"nums = {nums}")
    print(f"ans = {ans}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
