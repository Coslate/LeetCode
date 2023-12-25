from typing import Optional, List
import collections

class Solution:
    def rowCheck(self, board: List[List[str]], row_num: int, col_num: int) -> bool:
        for i in range(row_num):
            mem_dict = {}

            for j in range(col_num):
                if board[i][j] == ".":
                    next
                else:
                    if board[i][j] in mem_dict:
                        return False
                    else:
                        mem_dict[board[i][j]] = 1
        return True

    def colCheck(self, board: List[List[str]], row_num: int, col_num: int) -> bool:
        for j in range(col_num):
            mem_dict = {}

            for i in range(row_num):
                if board[i][j] == ".":
                    next
                else:
                    if board[i][j] in mem_dict:
                        return False
                    else:
                        mem_dict[board[i][j]] = 1

        return True

    def boxCheck(self, board: List[List[str]], row_num: int, col_num: int) -> bool:
        for i in range(3):
            for j in range(3):
                mem_dict = {}
                grid_i = i*3
                grid_j = j*3
                for k in range(3):
                    for r in range(3):
                        index_i = grid_i + k
                        index_j = grid_j + r
                        if board[index_i][index_j] == ".":
                            next
                        else:
                            if board[index_i][index_j] in mem_dict:
                                return False
                            else:
                                mem_dict[board[index_i][index_j]] = 1
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Matrix | Time: O(n) | Space: O(n)
        row_num = len(board)
        col_num = len(board[0])
        if not self.rowCheck(board, row_num, col_num):
            return False
        if not self.colCheck(board, row_num, col_num):
            return False
        if not self.boxCheck(board, row_num, col_num):
            return False

        return True

class OptSolution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Sliding Window | Time: O(n) | Space: O(1)
        # Same as above
        pass


