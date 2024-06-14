from typing import Optional, List, Tuple
import math
from numpy.linalg import matrix_power
import numpy as np

class UnionFind:
    def __init__(self, grid: List[List[str]]):
        self.count = 0
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.rank = []
        self.parent = []

        for i in range(self.rows):
            for j in range(self.cols):
                index = i*self.cols+j
                self.rank.append(0)
                if grid[i][j] == "1":
                    self.parent.append(index)
                    self.count += 1
                else:
                    self.parent.append(-1)

    def find(self, index: int):
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def union(self, index1: int, index2: int):
        root1 = self.find(index1)
        root2 = self.find(index2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1
            self.count -= 1

    def getCount(self):
        return self.count

class Solution:
    def withinRange(self, rows: int, cols: int, cur_pt: Tuple[int, int]) -> bool:
        if cur_pt[0] < rows and cur_pt[0] > -1 and cur_pt[1] < cols and cur_pt[1] > -1:
            return True
        else:
            return False

    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS | Time: O(m*n) | Space: O(m*n), n is the height of heights, and m is
        # the width of heights.
        if not grid:
            return 0

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        ans  = 0
        visited = {}

        def dfs(rows: int, cols: int, cur_pt: Tuple[int, int], visited: {}) -> None:
            if cur_pt in visited:
                return

            visited[cur_pt] = 1
            for direc_vec in direction:
                neighbor_pt = (cur_pt[0]+direc_vec[0], cur_pt[1]+direc_vec[1])
                if not self.withinRange(rows, cols, neighbor_pt):
                    continue
                if neighbor_pt in visited:
                    continue
                if grid[neighbor_pt[0]][neighbor_pt[1]] == "0":
                    continue

                dfs(rows, cols, neighbor_pt, visited)

        for i in range(rows):
            for j in range(cols):
                if (i, j) in visited or grid[i][j] == "0":
                    continue
                dfs(rows, cols, (i, j), visited)
                ans += 1

        return ans

class OptSolution:
    def withinRange(self, rows: int, cols: int, cur_pt: Tuple[int, int]) -> bool:
        if cur_pt[0] < rows and cur_pt[0] > -1 and cur_pt[1] < cols and cur_pt[1] > -1:
            return True
        else:
            return False

    def numIslands(self, grid: List[List[str]]) -> int:
        # UnionFind | Time: O(m*n) | Space: O(m*n), n is the height of heights, and m is
        # the width of heights.
        if grid is None or grid[0] is None:
            return 0

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])

        uf_data_structure = UnionFind(grid)
        for i in range(rows):
            for j in range(cols):
                index_cur_pt = i*cols+j
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    for dir_vec in direction:
                        neighbor_pt = (i+dir_vec[0], j+dir_vec[1])
                        index_neigh_pt = neighbor_pt[0]*cols + neighbor_pt[1]
                        if not self.withinRange(rows, cols, neighbor_pt):
                            continue
                        if grid[neighbor_pt[0]][neighbor_pt[1]] == "1":
                            uf_data_structure.union(index_neigh_pt, index_cur_pt)

        return uf_data_structure.getCount()



























