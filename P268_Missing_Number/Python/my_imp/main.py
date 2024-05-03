#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    nums = [3, 0, 1]
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"nums = {nums}")
    print(f"//------Checked-------//")
    output = sol.missingNumber(nums)
    output_opt = sol_opt.missingNumber(nums)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    nums = [0, 1]
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"nums = {nums}")
    print(f"//------Checked-------//")
    output = sol.missingNumber(nums)
    output_opt = sol_opt.missingNumber(nums)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    nums = [9,6,4,2,3,5,7,0,1]
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"nums = {nums}")
    print(f"//------Checked-------//")
    output = sol.missingNumber(nums)
    output_opt = sol_opt.missingNumber(nums)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
