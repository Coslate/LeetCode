from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import Counter, deque
import math
import numpy as np
import heapq
import random

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:    
        # Time: O(N!) | Space: O(N^2)
        # Backtracking
        # Where N is the number of Queens to be placed, also the widht and height of the board.
        # https://leetcode.com/problems/n-queens/editorial/?envType=problem-list-v2&envId=plakya4j

        ans = []
        state = [['.']*n for _ in range(n)]
        col_set = set()
        diag_set = set()
        anti_diag_set = set()

        def remove_queen(row=0, col=0, cur_diag=0, cur_anti_diag=0, col_set=set(), diag_set=set(), anti_diag_set=set(), state=[[]], ans=[]):
            state[row][col] = '.'
            col_set.remove(col)
            diag_set.remove(cur_diag)
            anti_diag_set.remove(cur_anti_diag)

        def place_queen(row=0, col=0, cur_diag=0, cur_anti_diag=0, col_set=set(), diag_set=set(), anti_diag_set=set(), state=[[]], ans=[]):
            state[row][col] = 'Q'
            col_set.add(col)
            diag_set.add(cur_diag)
            anti_diag_set.add(cur_anti_diag)

        def create_board(state:[[]]) -> [[]]:
            result = []
            for row in state:
                result.append(''.join(row))
            return result

        def backtracking(row=0, col_set=set(), diag_set=set(), anti_diag_set=set(), state=[[]], ans = []) -> None:
            if row == n:
                ans.append(create_board(state))
                return
                
            for col in range(n):
                cur_diag = row-col
                cur_anti_diag = row+col

                if col in col_set or cur_diag in diag_set or cur_anti_diag in anti_diag_set:
                    continue

                # Do the candidate
                place_queen(row, col, cur_diag, cur_anti_diag, col_set, diag_set, anti_diag_set, state, ans)

                # Keep exploring 
                backtracking(row+1, col_set, diag_set, anti_diag_set, state, ans)

                # Backtracking - remove the placed queen
                remove_queen(row, col, cur_diag, cur_anti_diag, col_set, diag_set, anti_diag_set, state, ans)


        backtracking(0, col_set, diag_set, anti_diag_set, state, ans)
        return ans