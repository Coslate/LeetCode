#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    numbers = [1, 2, 3, 4]
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"//------Checked-------//")
    output = sol.productExceptSelf(numbers)
    output_opt = sol_opt.productExceptSelf(numbers)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    numbers = [-1, 1, 0, -3, 3]
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"//------Checked-------//")
    output = sol.productExceptSelf(numbers)
    output_opt = sol_opt.productExceptSelf(numbers)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
