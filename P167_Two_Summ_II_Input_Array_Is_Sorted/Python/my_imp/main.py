#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    numbers = [2, 7, 11, 15]
    target = 9
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"target = {target}")
    print(f"//------Checked-------//")
    output = sol.twoSum(numbers, target)
    print(f"output = {output}")
    print(f"")
    print(f"")

    numbers = [2, 3, 4]
    target = 6
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"target = {target}")
    print(f"//------Checked-------//")
    output = sol.twoSum(numbers, target)
    print(f"output = {output}")
    print(f"")
    print(f"")

    numbers = [-1, 0]
    target = -1
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"target = {target}")
    print(f"//------Checked-------//")
    output = sol.twoSum(numbers, target)
    print(f"output = {output}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
