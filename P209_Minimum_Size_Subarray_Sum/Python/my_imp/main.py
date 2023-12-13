#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    numbers = [2, 3, 1, 2, 4, 3]
    target = 7
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"target = {target}")
    print(f"//------Checked-------//")
    output = sol.minSubArrayLen(target, numbers)
    print(f"output = {output}")
    print(f"")
    print(f"")

    numbers = [1, 4, 4]
    target = 4
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"target = {target}")
    print(f"//------Checked-------//")
    output = sol.minSubArrayLen(target, numbers)
    print(f"output = {output}")
    print(f"")
    print(f"")

    numbers = [1, 1, 1, 1, 1, 1, 1, 1]
    target = 11
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"target = {target}")
    print(f"//------Checked-------//")
    output = sol.minSubArrayLen(target, numbers)
    print(f"output = {output}")
    print(f"")
    print(f"")

    numbers = [12,28,83,4,25,26,25,2,25,25,25,12]
    target = 213
    print(f"//Case4:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"target = {target}")
    print(f"//------Checked-------//")
    output = sol.minSubArrayLen(target, numbers)
    print(f"output = {output}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
