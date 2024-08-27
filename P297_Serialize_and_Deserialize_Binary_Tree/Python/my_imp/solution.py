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

    def treeNode2List(self, root: Optional[TreeNode]) -> List[int|str]:
        queue = collections.deque([root])
        result_list = []

        while queue:
            top_root = queue.popleft()
            if top_root is None:
                result_list.append('null')
            else:
                result_list.append(top_root.val)
                queue.append(top_root.left)
                queue.append(top_root.right)

        return result_list

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        # Recursive Traversing - PreOrder | O(n) | O(n)
        # Where n is the size of nodes in the Binary Tree.
        serialized_result = []
        def rserialize(root: Optional[TreeNode]) -> None:
            if root is None:
                serialized_result.append('None'+',')
                return None

            serialized_result.append(str(root.val)+',')
            rserialize(root.left)
            rserialize(root.right)
        rserialize(root)
        return ''.join(serialized_result)

    def deserialize(self, data) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        # Recursive Traversing - PreOrder | O(n) | O(n)
        # Where n is the size of nodes in the Binary Tree.
        serialized_result = collections.deque(data.split(','))
        def rdeserialize(root: Optional[str]) -> Optional[TreeNode]:
            if root == 'None':
                serialized_result.popleft()
                return None

            root_val = int(serialized_result.popleft())
            root_node = TreeNode(root_val)

            root_node.left  = rdeserialize(serialized_result[0])
            root_node.right = rdeserialize(serialized_result[0])
            return root_node

        root_node = rdeserialize(serialized_result[0])
        return root_node

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




