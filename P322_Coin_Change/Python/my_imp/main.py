#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    nums = 2
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"nums = {nums}")
    print(f"//------Checked-------//")
    output = sol.climbStairs(nums)
    output_opt = sol_opt.climbStairs(nums)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    nums = 3
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"nums = {nums}")
    print(f"//------Checked-------//")
    output = sol.climbStairs(nums)
    output_opt = sol_opt.climbStairs(nums)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
