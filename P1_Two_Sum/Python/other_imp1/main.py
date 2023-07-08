#! /usr/bin/env python3

from solution import Solution

def main():
    sol = Solution()
    nums = [3, 2, 4]
    target = 6

    ans = sol.twoSum(nums, target)
    print(f"nums = {nums}, target = {target}")
    print(f"ans = {ans}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
