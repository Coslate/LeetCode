#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    numbers = [3, 4, 5, 1, 2]
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"//------Checked-------//")
    output = sol.findMin(numbers)
    print(f"output = {output}")
    print(f"")
    print(f"")

    numbers = [4, 5, 6, 7, 0, 1, 2]
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"//------Checked-------//")
    output = sol.findMin(numbers)
    print(f"output = {output}")
    print(f"")
    print(f"")

    numbers = [11, 13, 15, 17]
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"//------Checked-------//")
    output = sol.findMin(numbers)
    print(f"output = {output}")
    print(f"")
    print(f"")

    numbers = [2, 1]
    print(f"//Case4:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"//------Checked-------//")
    output = sol.findMin(numbers)
    print(f"output = {output}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
