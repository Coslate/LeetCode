from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import defaultdict
import math
import numpy as np
import heapq
import random

class Solution:
    def __init__(self):
        self.WHITE = 0
        self.GRAY  = 1
        self.BLACK = 2
        self.cycle_det = False

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:    
        # Time: O(V+E) | Space: O(V+E)
        # Graph DFS
        # Where V = len(numCourses), E = len(prerequisites)
        # https://leetcode.com/problems/course-schedule-ii/editorial/?envType=problem-list-v2&envId=plakya4j

        # Build adj list
        adj_list = defaultdict(list)
        for dst, src in prerequisites:
            adj_list[dst].append(src)


        # Check if there exist a cycle
        node_visited = [self.WHITE for _ in range(numCourses)]

        # DFS Traversal
        ans = []
        def dfs(node: int):
            if node_visited[node] == self.BLACK:
                return
            elif node_visited[node] == self.WHITE:
                node_visited[node] = self.GRAY

            if node in adj_list:
                for neighbor in adj_list[node]:
                    if node_visited[neighbor] == self.WHITE:
                        dfs(neighbor)
                    elif node_visited[neighbor] == self.GRAY:
                        self.cycle_det = True
                        return

            node_visited[node] = self.BLACK
            ans.append(node)
            return

        for i in range(numCourses):
            dfs(i)
            if self.cycle_det: break

        return [] if self.cycle_det else ans