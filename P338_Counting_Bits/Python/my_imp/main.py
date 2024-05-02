#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    n = 2
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"n = {n}")
    print(f"//------Checked-------//")
    output = sol.countBits(n)
    output_opt = sol_opt.countBits(n)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    n = 5
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"n = {n}")
    print(f"//------Checked-------//")
    output = sol.countBits(n)
    output_opt = sol_opt.countBits(n)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
