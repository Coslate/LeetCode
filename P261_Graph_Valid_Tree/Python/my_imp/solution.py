from typing import Optional, List, Tuple
import math
from numpy.linalg import matrix_power
import numpy as np

from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # DFS | Time: O(N) | Space: O(N), N is the number of nodes in edges.
        # Since E==N-1, so O(N+E) = O(N), if E!=N-1, then we can directly return False.

        #Step0. Valid tree should suffice two conditions:
                #1. Number of edges equals to number of vertex-1. 
                #2. The tree is fully connected, which means each node is reachable from a single start node.
        #Step1. Check if the number of edges, N, equals to n-1.
        if len(edges) != (n-1): return False

        #Step2. Construct adj_list to represent undirected graph.
        adj_list = {c:[] for c in range(n)}
        for x0, x1 in edges:
            adj_list[x0].append(x1)
            adj_list[x1].append(x0)

        #Step3. Use iterative-DFS to check whether there is a loop inside the undirected graph.
        seen_hash = {0}
        stack = deque([0])

        while(stack):
            top_pt = stack.pop()

            for neighnor in adj_list[top_pt]:
                if neighnor not in seen_hash:
                    seen_hash.add(neighnor)
                    stack.append(neighnor)

        return len(seen_hash) == n

class UnionFind:
    def __init__(self, n: int):
        self.parent = [c for c in range(n)]
        self.size = [1 for c in range(n)]

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

        if self.size[root1] < self.size[root2]:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]

        return True

class OptSolution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # UnionFind | Time: O(N*alpha(N)) | Space: O(N), N is the number of nodes in edges.
        # Since E==N-1, so O(N+E) = O(N), if E!=N-1, then we can directly return False.
        # Where alpha() is Inverse Ackermann Function. aplha(N) is no more than 5 with any of N, so it is almost constant.

        #Step0. Valid tree should suffice two conditions:
                #1. Number of edges equals to number of vertex-1. 
                #2. The tree is fully connected, which means all nodes are in a connected component. Once the two nodes of an edge inserting has the same root -> loop detected.
        #Step1. Check if the number of edges, N, equals to n-1.
        if len(edges) != n-1: return False

        #Step2. Check if an loop exists in the graph.
        union_find_data_structure = UnionFind(n)

        for x0, x1 in edges:
            if not union_find_data_structure.union(x0, x1):
                return False

        return True

