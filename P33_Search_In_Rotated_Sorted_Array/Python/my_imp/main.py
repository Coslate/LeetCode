#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    numbers = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"target = {target}")
    print(f"//------Checked-------//")
    output = sol.search(numbers, target)
    print(f"output = {output}")
    print(f"")
    print(f"")

    numbers = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"target = {target}")
    print(f"//------Checked-------//")
    output = sol.search(numbers, target)
    print(f"output = {output}")
    print(f"")
    print(f"")

    numbers = [1]
    target = 0
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"target = {target}")
    print(f"//------Checked-------//")
    output = sol.search(numbers, target)
    print(f"output = {output}")
    print(f"")
    print(f"")

    numbers = [1, 3]
    target = 3
    print(f"//Case4:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"target = {target}")
    print(f"//------Checked-------//")
    output = sol.search(numbers, target)
    print(f"output = {output}")
    print(f"")
    print(f"")

    numbers = [3, 1]
    target = 3
    print(f"//Case5:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"target = {target}")
    print(f"//------Checked-------//")
    output = sol.search(numbers, target)
    print(f"output = {output}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
