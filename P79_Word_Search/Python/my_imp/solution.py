from typing import Optional, List
import collections
import math

class Solution:
    def resetProcess(self, ans_list: List[List[str]], has_unvisit_neighbor: List[List[bool]], visit: List[List[bool]], stack_dfs: List[tuple[int, int]]) -> None:
        while len(ans_list) > 0:
            (idx_i, idx_j) = ans_list[-1]
            if has_unvisit_neighbor[idx_i][idx_j]:
                stack_dfs.append((idx_i, idx_j))
                break
            else:
                visit[idx_i][idx_j] = False
                ans_list.pop()

    def DFSCall(self, board: List[List[str]], word: str, i: int, j: int, visit: List[List[bool]], row_num: int, col_num: int, has_unvisit_neighbor: List[List[bool]]) -> bool:
        idx_i     = i
        idx_j     = j
        stack_dfs = [(idx_i, idx_j)]
        word_idx  = 0
        word_len  = len(word)
        ans       = False
        ans_list  = []

        while len(stack_dfs) > 0:
            (idx_i, idx_j) = stack_dfs.pop()
            if visit[idx_i][idx_j]:
                next

            visit[idx_i][idx_j] = True
            up_got    = False
            down_got  = False
            right_got = False
            left_got  = False

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

                check_idx_i = idx_i
                check_idx_j = idx_j+1
                if check_idx_j < col_num and visit[check_idx_i][check_idx_j] == False and board[check_idx_i][check_idx_j]==word[word_idx]:
                    stack_dfs.append((check_idx_i, check_idx_j))
                    right_got = True
                    if down_got:
                        has_unvisit_neighbor[idx_i][idx_j] = True

                check_idx_i = idx_i-1
                check_idx_j = idx_j
                if check_idx_i > -1 and visit[check_idx_i][check_idx_j] == False and board[check_idx_i][check_idx_j]==word[word_idx]:
                    stack_dfs.append((check_idx_i, check_idx_j))
                    up_got = True
                    if down_got | right_got:
                        has_unvisit_neighbor[idx_i][idx_j] = True

                check_idx_i = idx_i
                check_idx_j = idx_j-1
                if check_idx_j > -1 and visit[check_idx_i][check_idx_j] == False and board[check_idx_i][check_idx_j]==word[word_idx]:
                    stack_dfs.append((check_idx_i, check_idx_j))
                    left_got = True
                    if down_got | right_got | up_got:
                        has_unvisit_neighbor[idx_i][idx_j] = True

                if (not up_got) and (not down_got) and (not left_got) and (not right_got):
                    print(f"---Before resetProcess()---")
                    print(f"({idx_i}, {idx_j})")
                    print(f"stack_dfs = {stack_dfs}")
                    print(f"ans_list = {ans_list}")
                    print(f"has_unvisit_neighbor = {has_unvisit_neighbor}")
                    print(f"visit = {visit}")
                    self.resetProcess(ans_list, has_unvisit_neighbor, visit, stack_dfs)
                    print(f"---After resetProcess()---")
                    print(f"({idx_i}, {idx_j})")
                    print(f"stack_dfs = {stack_dfs}")
                    print(f"ans_list = {ans_list}")
                    print(f"has_unvisit_neighbor = {has_unvisit_neighbor}")
                    print(f"visit = {visit}")

        return ans

    def exist(self, board: List[List[str]], word: str) -> bool:
        # Matrix | Time: O(n^2) | Space: O(1)
        row_num   = len(board)
        col_num   = len(board[0])

        for i in range(row_num):
            for j in range(col_num):
                if board[i][j] == word[0]:
                    visit = [[False for j in range(col_num)] for i in range(row_num)]
                    has_unvisit_neighbor = [[False for j in range(col_num)] for i in range(row_num)]
                    ans = self.DFSCall(board, word, i, j, visit, row_num, col_num, has_unvisit_neighbor)
                    if ans:
                        return True

        return False

class OptSolution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Matrix | Time: O(n^2) | Space: O(1)
        pass
