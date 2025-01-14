from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import Counter, deque
import math
import numpy as np
import heapq
import random

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Time: O(NM) | Space: O(NM)
        # BFS
        # Where N is the number of rows of grid.
        # Where M is the number of cols of grid.
        # https://leetcode.com/problems/rotting-oranges/editorial/?envType=problem-list-v2&envId=plakya4j

        rows = len(grid)
        cols = len(grid[0])
        fresh_fruit = 0
        queue = deque()
        elapsed_minutes = -1

        # Calculating fresh_fruit, appending rotting coordinates
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_fruit += 1

        # Mark the end of one minutes                    
        queue.append((-1, -1))

        while queue:
            r, c = queue.popleft()

            if r == -1:
                elapsed_minutes += 1
                if queue:#Still have unconsumed oranges
                    queue.append((-1, -1))
            else:
                directions = [(+1, 0), (-1, 0), (0, +1), (0, -1)]
                for d in directions:
                    explore_r = r + d[0]
                    explore_c = c + d[1]

                    if -1 < explore_r < rows and -1 < explore_c < cols:
                        if grid[explore_r][explore_c] == 1:
                            grid[explore_r][explore_c] = 2
                            queue.append((explore_r, explore_c))
                            fresh_fruit -= 1

        return elapsed_minutes if fresh_fruit == 0 else -1

