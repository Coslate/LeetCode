#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    numbers = [1, 2, 3, 1]
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"//------Checked-------//")
    output = sol.containsDuplicate(numbers)
    print(f"output = {output}")
    print(f"")
    print(f"")

    numbers = [1, 2, 3, 4]
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"//------Checked-------//")
    output = sol.containsDuplicate(numbers)
    print(f"output = {output}")
    print(f"")
    print(f"")

    numbers = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"//------Checked-------//")
    output = sol.containsDuplicate(numbers)
    print(f"output = {output}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
