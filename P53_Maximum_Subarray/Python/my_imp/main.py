#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"//------Checked-------//")
    output = sol.maxSubArray(numbers)
    output_opt = sol_opt.maxSubArray(numbers)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    numbers = [1]
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"//------Checked-------//")
    output = sol.maxSubArray(numbers)
    output_opt = sol_opt.maxSubArray(numbers)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    numbers = [5, 4, -1, 7, 8]
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"//------Checked-------//")
    output = sol.maxSubArray(numbers)
    output_opt = sol_opt.maxSubArray(numbers)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
