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

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Iterative Traversing | O(n) | O(n)
        # Where n is the size of nodes in the Binary Tree.

        queue1 = []
        queue2 = []
        queue1.append(p)
        queue2.append(q)

        while queue1 and queue2:
            extracted_root1 = queue1.pop(0)
            extracted_root2 = queue2.pop(0)

            if extracted_root1 is None and extracted_root2 is not None:
                return False

            if extracted_root1 is not None and extracted_root2 is None:
                return False

            if extracted_root1 is None and extracted_root2 is None:
                continue

            if extracted_root1.val != extracted_root2.val:
                return False

            queue1.append(extracted_root1.left)
            queue1.append(extracted_root1.right)
            queue2.append(extracted_root2.left)
            queue2.append(extracted_root2.right)

        if queue1 or queue2:
            return False

        return True

class OptSolution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Iterative Traversing | O(n) | O(n)
        # Where n is the size of nodes in the Binary Tree.
        pass

