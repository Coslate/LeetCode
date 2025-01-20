from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import Counter, deque
import math
import numpy as np
import heapq
import random

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Time: O(m*n) | Space: O(m*n)
        # DFS + Memorization
        # Where m*n is the matrix size.
        # https://leetcode.com/problems/longest-increasing-path-in-a-matrix/editorial/?envType=problem-list-v2&envId=plakya4j

        m = len(matrix)
        if m == 0: return 0

        n = len(matrix[0])
        cache = [[None]*n for _ in range(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, self.dfs(i, j, matrix, cache, m, n))

        return ans

    def dfs(self, i: int, j: int, matrix: List[List[int]], cache: List[List[int]], m: int, n: int) -> int:
        if cache[i][j] != None: return cache[i][j]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        path_max = -1
        got_path = False
        for d in dirs:
            r = i + d[0]
            c = j + d[1]

            if 0 <= r < m and 0 <= c < n and matrix[i][j]>matrix[r][c]:
                path_max = max(path_max, self.dfs(r, c, matrix, cache, m, n))
                got_path = True

        cache[i][j] = 1+path_max if got_path else 1
        return cache[i][j]
            






