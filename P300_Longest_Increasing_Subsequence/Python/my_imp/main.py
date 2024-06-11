#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    nums = [10,9,2,5,3,7,101,18]
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"nums = {nums}")
    print(f"//------Checked-------//")
    output = sol.lengthOfLIS(nums)
    output_opt = sol_opt.lengthOfLIS(nums)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    nums = [0, 1, 0, 3, 2, 3]
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"nums = {nums}")
    print(f"//------Checked-------//")
    output = sol.lengthOfLIS(nums)
    output_opt = sol_opt.lengthOfLIS(nums)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"output = {output}")
    print(f"")
    print(f"")

    nums = [7,7,7,7,7,7,7]
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"nums = {nums}")
    print(f"//------Checked-------//")
    output = sol.lengthOfLIS(nums)
    output_opt = sol_opt.lengthOfLIS(nums)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"output = {output}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
