from typing import Optional, List
import collections
import math

class Solution:
    def DFSCall(self, board: List[List[str]], word: str, i: int, j: int, visit: List[List[bool]], row_num: int, col_num: int) -> bool:
        idx_i     = i
        idx_j     = j
        stack_dfs = [(idx_i, idx_j)]
        word_idx  = 0
        word_len  = len(word)
        ans       = False

        while len(stack_dfs) > 0:
            (idx_i, idx_j) = stack_dfs.pop()
            visit[idx_i][idx_j] = True
            print(f"idx_i, idx_j = ({idx_i}, {idx_j})")
            print(f"stack_dfs = {stack_dfs}, word_idx = {word_idx}")

            if board[idx_i][idx_j] == word[word_idx]:
                print(f"({idx_i}, {idx_j}), {board[idx_i][idx_j]}")
                word_idx += 1
                if word_idx == word_len:
                    ans = True
                    break

                if idx_i+1 < row_num and visit[idx_i+1][idx_j] == False:
                    stack_dfs.append((idx_i+1, idx_j))
                if idx_j+1 < col_num and visit[idx_i][idx_j+1] == False:
                    stack_dfs.append((idx_i, idx_j+1))
                if idx_i-1 > -1 and visit[idx_i-1][idx_j] == False:
                    stack_dfs.append((idx_i-1, idx_j))
                if idx_j-1 > -1 and visit[idx_i][idx_j-1] == False:
                    stack_dfs.append((idx_i, idx_j-1))

        return ans

    def exist(self, board: List[List[str]], word: str) -> bool:
        # Matrix | Time: O(n^2) | Space: O(1)
        row_num   = len(board)
        col_num   = len(board[0])
        visit     = [[False for j in range(col_num)] for i in range(row_num)]

        for i in range(row_num):
            for j in range(col_num):
                if visit[i][j] == False:
                    ans = self.DFSCall(board, word, i, j, visit, row_num, col_num)

        return ans

class OptSolution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Matrix | Time: O(n^2) | Space: O(1)
        pass
