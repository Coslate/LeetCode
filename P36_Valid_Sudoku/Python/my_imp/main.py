#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"board = {board}")
    print(f"//------Checked-------//")
    #output = sol.isValidSudoku(board)
    output = sol_opt.isValidSudoku(board)
    print(f"output = {output}")
    print(f"")
    print(f"")

    board = [["8","3",".",".","7",".",".",".","."]
             ,["6",".",".","1","9","5",".",".","."]
             ,[".","9","8",".",".",".",".","6","."]
             ,["8",".",".",".","6",".",".",".","3"]
             ,["4",".",".","8",".","3",".",".","1"]
             ,["7",".",".",".","2",".",".",".","6"]
             ,[".","6",".",".",".",".","2","8","."]
             ,[".",".",".","4","1","9",".",".","5"]
             ,[".",".",".",".","8",".",".","7","9"]]

    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"board = {board}")
    print(f"//------Checked-------//")
    #output = sol.isValidSudoku(board)
    output = sol_opt.isValidSudoku(board)
    print(f"output = {output}")
    print(f"")
    print(f"")



#---------------Execution---------------#
if __name__ == '__main__':
    main()
