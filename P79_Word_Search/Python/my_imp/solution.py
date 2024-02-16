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
        ans_list  = []

        while len(stack_dfs) > 0:
            (idx_i, idx_j) = stack_dfs.pop()
            visit[idx_i][idx_j] = True
            up_got    = False
            down_got  = False
            right_got = False
            left_got  = False
            #print(f"pop({idx_i}, {idx_j})")

            if board[idx_i][idx_j] == word[word_idx]:
                ans_list.append((idx_i, idx_j))
                word_idx += 1
                if word_idx == word_len:
                    ans = True
                    break

                check_idx_i = idx_i+1
                check_idx_j = idx_j
                if check_idx_i < row_num and visit[check_idx_i][check_idx_j] == False and board[check_idx_i][check_idx_j]==word[word_idx]:
                    stack_dfs.append((check_idx_i, check_idx_j))
                    down_got = True
                    #print(f"append: ({check_idx_i}, {check_idx_j})")

                check_idx_i = idx_i
                check_idx_j = idx_j+1
                if check_idx_j < col_num and visit[check_idx_i][check_idx_j] == False and board[check_idx_i][check_idx_j]==word[word_idx]:
                    stack_dfs.append((check_idx_i, check_idx_j))
                    right_got = True
                    #print(f"append: ({check_idx_i}, {check_idx_j})")

                check_idx_i = idx_i-1
                check_idx_j = idx_j
                if check_idx_i > -1 and visit[check_idx_i][check_idx_j] == False and board[check_idx_i][check_idx_j]==word[word_idx]:
                    stack_dfs.append((check_idx_i, check_idx_j))
                    up_got = True
                    #print(f"append: ({check_idx_i}, {check_idx_j})")

                check_idx_i = idx_i
                check_idx_j = idx_j-1
                if check_idx_j > -1 and visit[check_idx_i][check_idx_j] == False and board[check_idx_i][check_idx_j]==word[word_idx]:
                    stack_dfs.append((check_idx_i, check_idx_j))
                    left_got = True
                    #print(f"append: ({check_idx_i}, {check_idx_j})")

                if (not up_got) and (not down_got) and (not left_got) and (not right_got):
                    (_i, _j) = stack_dfs.pop()
                    (_k, _m) = ans_list.pop()

        return ans

    def exist(self, board: List[List[str]], word: str) -> bool:
        # Matrix | Time: O(n^2) | Space: O(1)
        row_num   = len(board)
        col_num   = len(board[0])

        for i in range(row_num):
            for j in range(col_num):
                if board[i][j] == word[0]:
                    visit = [[False for j in range(col_num)] for i in range(row_num)]
                    ans = self.DFSCall(board, word, i, j, visit, row_num, col_num)
                    if ans:
                        return True

        return False

class OptSolution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Matrix | Time: O(n^2) | Space: O(1)
        pass
