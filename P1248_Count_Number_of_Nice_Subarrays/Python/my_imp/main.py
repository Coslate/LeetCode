#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    numbers = [1, 1, 2, 1, 1]
    k = 3
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"k = {k}")
    print(f"//------Checked-------//")
    output = sol.numberOfSubarrays(numbers, k)
    print(f"output = {output}")
    print(f"")
    print(f"")

    numbers = [2, 4, 6]
    k = 1
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"k = {k}")
    print(f"//------Checked-------//")
    output = sol.numberOfSubarrays(numbers, k)
    print(f"output = {output}")
    print(f"")
    print(f"")

    numbers = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
    k = 2
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"numbers = {numbers}")
    print(f"k = {k}")
    print(f"//------Checked-------//")
    output = sol.numberOfSubarrays(numbers, k)
    print(f"output = {output}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
