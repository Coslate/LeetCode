from typing import Optional, List
import collections
import math

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Matrix | Time: O(n^2) | Space: O(1)
        row_num = len(board)
        col_num = len(board[0])

        for i in range(row_num):
            for j in range(col_num):
                if visit[i][j] == False:
                    ans = DFS_call(board, word, i, j)
                elif visit[i][j] == True and got_mask[i][j] == True:
                    if i+1 < row_num and visit[i+1][j] == False:
                        ans = DFS_call(board, word, i+1, j)
                    elif j+1 < col_num and visit[i][j+1] == False:
                        ans = DFS_call(board, word, i, j+1)
                    elif i-1 >= 0 and visit[i-1][j] == False:
                        ans = DFS_call(board, word, i-1, j)
                    elif j-1 >= 0 and visit[i][j-1] == False:
                        ans = DFS_call(board, word, i, j-1)



class OptSolution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Matrix | Time: O(n^2) | Space: O(1)
        pass
