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

    board = [
                ["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]
            ]
    word = "SEE"

    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"board = {board}")
    print(f"word  = {word}")
    print(f"//------Checked-------//")
    ans = sol.exist(board, word)
    print(f"ans = {ans}")
    print(f"")
    print(f"")

    board = [
                ["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]
            ]
    word = "ABCB"

    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"board = {board}")
    print(f"word  = {word}")
    print(f"//------Checked-------//")
    ans = sol.exist(board, word)
    print(f"ans = {ans}")
    print(f"")
    print(f"")

    board = [
                ["a","b"]
            ]
    word = "ba"

    print(f"//Case4:")
    print(f"//------Original-------//")
    print(f"board = {board}")
    print(f"word  = {word}")
    print(f"//------Checked-------//")
    ans = sol.exist(board, word)
    print(f"ans = {ans}")
    print(f"")
    print(f"")

    board =  [
                ["a","b"],
                ["c","d"]
            ]
    word = "acdb"

    print(f"//Case5:")
    print(f"//------Original-------//")
    print(f"board = {board}")
    print(f"word  = {word}")
    print(f"//------Checked-------//")
    ans = sol.exist(board, word)
    print(f"ans = {ans}")
    print(f"")
    print(f"")

    board = [
                ["C","A","A"],
                ["A","A","A"],
                ["B","C","D"]
            ]

    word = "AAB"

    print(f"//Case6:")
    print(f"//------Original-------//")
    print(f"board = {board}")
    print(f"word  = {word}")
    print(f"//------Checked-------//")
    ans = sol.exist(board, word)
    print(f"ans = {ans}")
    print(f"")
    print(f"")

    board = [
                ["A","B","C","E"],
                ["S","F","E","S"],
                ["A","D","E","E"]
            ]    
    word = "ABCESEEEFS"

    print(f"//Case7:")
    print(f"//------Original-------//")
    print(f"board = {board}")
    print(f"word  = {word}")
    print(f"//------Checked-------//")
    ans = sol.exist(board, word)
    print(f"ans = {ans}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
