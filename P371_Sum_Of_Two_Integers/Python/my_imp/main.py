#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    a = 1
    b = 2
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"sum: {a}, {b}")
    print(f"//------Checked-------//")
    output = sol.getSum(a, b)
    print(f"output = {output}")
    print(f"")
    print(f"")

    a = 2
    b = 3
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"sum: {a}, {b}")
    print(f"//------Checked-------//")
    output = sol.getSum(a, b)
    print(f"output = {output}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
