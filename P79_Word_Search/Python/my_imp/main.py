#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    board = [
                ["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]
    ]

    word = "ABCCED"

    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"board = {board}")
    print(f"word  = {word}")
    print(f"//------Checked-------//")
    ans = sol.exist(board, word)
    print(f"ans = {ans}")
    print(f"")
    print(f"")

'''
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
'''


#---------------Execution---------------#
if __name__ == '__main__':
    main()
