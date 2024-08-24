from typing import Optional, List, Tuple, Dict, Deque, Set, Self
import collections
import math
from numpy.linalg import matrix_power
import numpy as np
import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, root: List[TreeNode]) -> Dict[int, TreeNode]:
        map_idx_node: Dict[int, TreeNode] = {}

        for idx, node_val in enumerate(root):
            if node_val is None or node_val == 'null':
                map_idx_node[idx] = None
                continue

            new_node = TreeNode(node_val)
            map_idx_node[idx] = new_node

        for idx, node_val in enumerate(root):
            if node_val is None or node_val == 'null':
                continue

            left_child_idx = idx*2+1
            right_child_idx = idx*2+2

            if left_child_idx < len(root):
                map_idx_node[idx].left = map_idx_node[left_child_idx]
            else:
                map_idx_node[idx].left = None

            if right_child_idx < len(root):
                map_idx_node[idx].left = map_idx_node[right_child_idx]
            else:
                map_idx_node[idx].left = None

        return map_idx_node

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative Traversing | O(n) | O(n)
        # Where n is the size of nodes in the Binary Tree.

        queue = []
        if root is not None:
            queue.append((1, root))

        depth = 0
        while queue:
            prev_depth, prev_root = queue.pop(0)
            if prev_root is not None:
                depth = max(depth, prev_depth)
                queue.append((prev_depth+1, prev_root.left))
                queue.append((prev_depth+1, prev_root.right))

        return depth

class OptSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Chunked Transfer Encoding | O(n) | O(k)
        pass

