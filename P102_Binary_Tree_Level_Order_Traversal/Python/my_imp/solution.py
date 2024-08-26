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
                map_idx_node[idx].right = map_idx_node[right_child_idx]
            else:
                map_idx_node[idx].right = None

        return map_idx_node

    def printTree(self, root: Optional[TreeNode]) -> None:
        # Level Travesal
        if root is None:
            print(f"------------")
            return

        old_level = 0
        queue = collections.deque([(old_level, root)])
        expected_node_num = 1
        node_num_cnt = 0

        while queue:
            top_level, top_root = queue.popleft()

            if top_root != None:
                print(f"node({top_root.val})")
                if top_root.left:  queue.append((top_level+1, top_root.left))
                if top_root.right: queue.append((top_level+1, top_root.right))

            node_num_cnt += 1
            if node_num_cnt == expected_node_num:
                node_num_cnt = 0
                expected_node_num *= 2
                print(f"------------")

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Recursive Traversing | O(n) | O(n)
        # Where n is the size of nodes in the Binary Tree.
        level_node = []

        def traverseLevels(root: Optional[TreeNode], level: int) -> None:
            if root is None:
                return

            if len(level_node) == level:
                level_node.append([])

            level_node[level].append(root.val)
            traverseLevels(root.left, level+1)
            traverseLevels(root.right, level+1)

        traverseLevels(root, 0)
        return level_node

class OptSolution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Iterative Traversing | O(n) | O(n)
        # Where n is the size of nodes in the Binary Tree.
        if root is None:
            return []

        level_node = []
        queue = collections.deque([root])

        while queue:
            level_length = len(queue)
            level_node.append([])

            for i in range(level_length):
                top_root = queue.popleft()
                level_node[-1].append(top_root.val)
                if top_root.left:
                    queue.append(top_root.left)
                if top_root.right:
                    queue.append(top_root.right)

        return level_node




