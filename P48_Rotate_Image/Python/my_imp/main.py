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
    sol.rotate(matrix)
    print(f"ans = {matrix}")
    print(f"")
    print(f"")

    matrix = [
                [5,  1,  9,  11],
                [2,  4,  8,  10],
                [13, 3,  6,   7],
                [15, 14, 12, 16]
            ]

    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"matrix = {matrix}")
    print(f"//------Checked-------//")
    sol.rotate(matrix)
    print(f"ans = {matrix}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
