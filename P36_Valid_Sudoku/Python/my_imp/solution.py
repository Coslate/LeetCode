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
        pass

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Sliding Window | Time: O(n) | Space: O(1)
        pass

class OptSolution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Sliding Window | Time: O(n) | Space: O(1)
        # Same as above
        pass


