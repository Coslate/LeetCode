#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    matrix = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]

    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"matrix = {matrix}")
    print(f"//------Checked-------//")
    ans = sol.spiralOrder(matrix)
    print(f"ans = {ans}")
    print(f"")
    print(f"")

    matrix = [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]
            ]

    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"matrix = {matrix}")
    print(f"//------Checked-------//")
    ans = sol.spiralOrder(matrix)
    print(f"ans = {ans}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
