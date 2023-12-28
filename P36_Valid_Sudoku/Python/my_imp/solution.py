from typing import Optional, List
import collections

class Solution:
    def rowCheck(self, board: List[List[str]], row_num: int, col_num: int) -> bool:
        for i in range(row_num):
            mem_dict = {}

            for j in range(col_num):
                if board[i][j] == ".":
                    continue
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
                    continue
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
                            continue
                        else:
                            if board[index_i][index_j] in mem_dict:
                                return False
                            else:
                                mem_dict[board[index_i][index_j]] = 1
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Matrix | Time: O(n^2) | Space: O(n^2)
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
    def getBit(self, x: int, val: int) -> int:
        return (x>>val) & 1

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Bitmasking | Time: O(n^2) | Space: O(n)
        row_num = len(board)
        col_num = len(board[0])
        row_check_bitarr = [0]*row_num
        col_check_bitarr = [0]*col_num
        box_check_bitarr = [0]*(int)((row_num/3)*(col_num/3))

        for i in range(row_num):
            for j in range(col_num):
                if board[i][j] == ".":
                    continue

                val = ord(board[i][j]) - ord('0')
                box_pos = (i//3)*3 + (j//3)
                if self.getBit(row_check_bitarr[i], val) or self.getBit(col_check_bitarr[j], val) or self.getBit(box_check_bitarr[box_pos], val):
                    return False
                val_bit = (1<<val)
                row_check_bitarr[i] |= val_bit
                col_check_bitarr[j] |= val_bit
                box_check_bitarr[box_pos] |= val_bit

        return True

