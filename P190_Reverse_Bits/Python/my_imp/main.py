#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    nums = int("00000010100101000001111010011100", 2)
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"nums = {nums}")
    print(f"//------Checked-------//")
    output = sol.reverseBits(nums)
    output_opt = sol_opt.reverseBits(nums)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    nums = int("11111111111111111111111111111101", 2)
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"nums = {nums}")
    print(f"//------Checked-------//")
    output = sol.reverseBits(nums)
    output_opt = sol_opt.reverseBits(nums)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
