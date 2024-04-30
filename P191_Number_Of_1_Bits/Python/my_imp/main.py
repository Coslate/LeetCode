#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    n = 11
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"n = {n}")
    print(f"//------Checked-------//")
    output = sol.hammingWeight(n)
    output_opt = sol_opt.hammingWeight(n)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    n = 128
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"n = {n}")
    print(f"//------Checked-------//")
    output = sol.hammingWeight(n)
    output_opt = sol_opt.hammingWeight(n)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    n = 2147483645
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"n = {n}")
    print(f"//------Checked-------//")
    output = sol.hammingWeight(n)
    output_opt = sol_opt.hammingWeight(n)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
