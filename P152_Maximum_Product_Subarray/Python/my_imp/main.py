#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    numbers = [2, 3, -2, 4]
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"//------Checked-------//")
    output = sol.maxProduct(numbers)
    output_opt = sol_opt.maxProduct(numbers)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    numbers = [-2, 0, -1]
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"//------Checked-------//")
    output = sol.maxProduct(numbers)
    output_opt = sol_opt.maxProduct(numbers)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    numbers = [3, -1, 4]
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"//------Checked-------//")
    output = sol.maxProduct(numbers)
    output_opt = sol_opt.maxProduct(numbers)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    numbers = [2, -5, -2, -4, 3]
    print(f"//Case4:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"//------Checked-------//")
    output = sol.maxProduct(numbers)
    output_opt = sol_opt.maxProduct(numbers)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
