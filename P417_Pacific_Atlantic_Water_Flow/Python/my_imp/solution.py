from typing import Optional, List, Tuple
import math
from numpy.linalg import matrix_power
import numpy as np

class Solution:
    def withinRange(self, rows: int, cols: int, cur_pt: Tuple[int, int]) -> bool:
        if cur_pt[0] < rows and cur_pt[0] > -1 and cur_pt[1] < cols and cur_pt[1] > -1:
            return True
        else:
            return False

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # BFS | Time: O(m*n) | Space: O(m*n), n is the height of heights, and m is
        # the width of heights.
        if heights is None or heights[0] is None:
            return None

        visited_twice    = []
        pacific_visited  = {}
        atlantic_visited = {}
        pacific_queue    = []
        atlantic_queue   = []
        rows = len(heights)
        cols = len(heights[0])
        neighbor_vec = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        #Initialize
        for i in range(rows):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, cols-1))

        for j in range(1, cols):
            pacific_queue.append((0, j))
            atlantic_queue.append((rows-1, j-1))

        #BFS - pacific
        while len(pacific_queue) != 0:
            cur_pt = pacific_queue.pop(0)
            pacific_visited[cur_pt] = 1
            for direction in neighbor_vec:
                neighbor_pt = (cur_pt[0]+direction[0], cur_pt[1]+direction[1])
                if not self.withinRange(rows, cols, neighbor_pt):
                    continue
                if neighbor_pt in pacific_visited:
                    continue
                if heights[cur_pt[0]][cur_pt[1]] > heights[neighbor_pt[0]][neighbor_pt[1]]:
                    continue
                pacific_queue.append(neighbor_pt)

        #BFS - atlantic
        while len(atlantic_queue) != 0:
            cur_pt = atlantic_queue.pop(0)
            atlantic_visited[cur_pt] = 1
            for direction in neighbor_vec:
                neighbor_pt = (cur_pt[0]+direction[0], cur_pt[1]+direction[1])
                if not self.withinRange(rows, cols, neighbor_pt):
                    continue
                if neighbor_pt in atlantic_visited:
                    continue
                if heights[cur_pt[0]][cur_pt[1]] > heights[neighbor_pt[0]][neighbor_pt[1]]:
                    continue
                atlantic_queue.append(neighbor_pt)

        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacific_visited and (i, j) in atlantic_visited:
                    visited_twice.append([i, j])

        return visited_twice

class OptSolution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # BFS | Time: O() | Space: O(), n is the height of heights, and m is
        # the width of heights.
        pass

