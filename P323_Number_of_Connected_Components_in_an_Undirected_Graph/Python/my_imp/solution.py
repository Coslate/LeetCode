from typing import Optional, List, Tuple, Dict, Deque, Set
import math
from numpy.linalg import matrix_power
import numpy as np

from collections import deque

class Solution:
    def DFSIterative(self, stack: Deque[int], seen_set: Set[int], adj_list: Dict[int, List[int]]) -> None:
        while(stack):
            top_pt = stack.pop()

            for neighnor in adj_list[top_pt]:
                if neighnor not in seen_set:
                    seen_set.add(neighnor)
                    stack.append(neighnor)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS | Time: O(V+E) | Space: O(V+E),
        # V is the number of nodes, n.
        # E is the number of edge in edges.

        #Step0. Construct adj_list to represent undirected graph.
        adj_list = {c:[] for c in range(n)}
        vertex_list = [pt for pt in range(n)]

        for x0, x1 in edges:
            adj_list[x0].append(x1)
            adj_list[x1].append(x0)

        #Step1. Use iterative-DFS to check how many connected components in the graph.
        seen_set = set()
        stack = deque([])
        counter = 0

        for v in vertex_list:
            if v not in seen_set:
                stack.append(v)
                seen_set.add(v)
                self.DFSIterative(stack, seen_set, adj_list)
                counter += 1

        return counter

class UnionFind:
    def __init__(self, n: int):
        self.parent = [c for c in range(n)]
        self.rank = [1 for c in range(n)]

    def find(self, A: int):
        #Step1. Find the root.
        root = A
        while(self.parent[root] != root):
            root = self.parent[root]

        #Step2. Compress the path.
        pt = A
        while(self.parent[pt] != root):
            old_root = self.parent[pt]
            self.parent[pt] = root
            pt = old_root

        return root

    def union(self, A: int, B: int) -> bool:
        root1 = self.find(A)
        root2 = self.find(B)

        if root1 == root2:
            return False

        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

        return True

class OptSolution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # UnionFind | Time: O(V + E*alpha(V)) | Space: O(V).
        # V is the number of vertexes, n.
        # E is the number of edges in edges[].
        # Where alpha() is Inverse Ackermann Function. aplha(N) is no more than 5 with any of N, so it is almost constant.

        #Step0. Setup Union Find data structure.
        union_find_data_structure = UnionFind(n)

        #Step1. Union points in all the edges, and counter-- once two points with different roots union.
        counter = n
        for x0, x1 in edges:
            if union_find_data_structure.union(x0, x1):
                counter -= 1

        return counter

