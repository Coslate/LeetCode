#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    matrix = [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
            ]

    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"matrix = {matrix}")
    print(f"//------Checked-------//")
    #sol.setZeroes(matrix)
    sol_opt.setZeroes(matrix)
    print(f"matrix = {matrix}")
    print(f"")
    print(f"")

    matrix = [
                [0, 1, 2, 0],
                [3, 4, 5, 2],
                [1, 3, 1, 5]
            ]

    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"matrix = {matrix}")
    print(f"//------Checked-------//")
    #sol.setZeroes(matrix)
    sol_opt.setZeroes(matrix)
    print(f"matrix = {matrix}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
