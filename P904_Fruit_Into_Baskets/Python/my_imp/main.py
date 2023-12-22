#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    fruits = [1, 2, 1]
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"fruits = {fruits}")
    print(f"//------Checked-------//")
    output = sol.totalFruit(fruits)
    print(f"output = {output}")
    print(f"")
    print(f"")

    fruits = [0, 1, 2, 2]
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"fruits = {fruits}")
    print(f"//------Checked-------//")
    output = sol.totalFruit(fruits)
    print(f"output = {output}")
    print(f"")
    print(f"")

    fruits = [1, 2, 3, 2, 2]
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"fruits = {fruits}")
    print(f"//------Checked-------//")
    output = sol.totalFruit(fruits)
    print(f"output = {output}")
    print(f"")
    print(f"")

    fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    print(f"//Case4:")
    print(f"//------Original-------//")
    print(f"fruits = {fruits}")
    print(f"//------Checked-------//")
    output = sol.totalFruit(fruits)
    print(f"output = {output}")
    print(f"")
    print(f"")

    fruits = [0, 1, 6, 6, 4, 4, 6]
    print(f"//Case5:")
    print(f"//------Original-------//")
    print(f"fruits = {fruits}")
    print(f"//------Checked-------//")
    output = sol.totalFruit(fruits)
    print(f"output = {output}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
