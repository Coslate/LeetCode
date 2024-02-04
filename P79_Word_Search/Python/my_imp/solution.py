from typing import Optional, List
import collections
import math

class Solution:
    def DFSCall(self, board: List[List[str]], word: str, i: int, j:int, word_idx: int, got_mask: List[List[bool]], visit: List[List[bool]]) -> (bool, int):
        visit[i][j] = True
        ans = []

        while True:
            pass

        return (ans, word_idx)
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Matrix | Time: O(n^2) | Space: O(1)
        row_num   = len(board)
        col_num   = len(board[0])
        got_mask  = [[False for j in range(col_num)] for i in range(row_num)]
        visit     = [[False for j in range(col_num)] for i in range(row_num)]
        word_idx  = 0

        for i in range(row_num):
            for j in range(col_num):
                if visit[i][j] == False:
                    (ans, word_idx) = self.DFSCall(board, word, i, j, word_idx, got_mask, visit)
                elif visit[i][j] == True and got_mask[i][j] == True:
                    if i+1 < row_num and visit[i+1][j] == False:
                        (ans, word_idx) = self.DFSCall(board, word, i+1, j, word_idx, got_mask, visit)
                    elif j+1 < col_num and visit[i][j+1] == False:
                        (ans, word_idx) = self.DFSCall(board, word, i, j+1, word_idx, got_mask, visit)
                    elif i-1 >= 0 and visit[i-1][j] == False:
                        (ans, word_idx) = self.DFSCall(board, word, i-1, j, word_idx, got_mask, visit)
                    elif j-1 >= 0 and visit[i][j-1] == False:
                        (ans, word_idx) = self.DFSCall(board, word, i, j-1, word_idx, got_mask, visit)

class OptSolution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Matrix | Time: O(n^2) | Space: O(1)
        pass
