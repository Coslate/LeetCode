from typing import Optional, List, Tuple, Dict, Deque, Set, Self
import collections
import math
import numpy as np
import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBSTIterative(self, root: Optional[TreeNode], min_range: float, max_range: float) -> bool:
        stack = [(root, min_range, max_range)]
        while stack:
            cur_root, cur_min, cur_max = stack.pop()
            if cur_root is None:
                continue

            if cur_root.val >= cur_max or cur_root.val <= cur_min:
                return False

            stack.append((cur_root.left, cur_min, cur_root.val))
            stack.append((cur_root.right, cur_root.val, cur_max))
        return True

    def isValidBSTRecursive(self, root: Optional[TreeNode], min_range: float, max_range: float) -> bool:
        # Empty tree is valid BST.
        if root is None:
            return True

        if root.val >= max_range or root.val <= min_range:
            return False

        return self.isValidBSTRecursive(root.left, min_range, root.val) and self.isValidBSTRecursive(root.right, root.val, max_range)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Range Check | Time: O(n) | Space: O(n)
        # Where n is the size of nodes in the Binary Tree

        # Method1 Recursive
        #return self.isValidBSTRecursive(root, -math.inf, math.inf)

        # Method2 Iterative
        return self.isValidBSTIterative(root, -math.inf, math.inf)

    def buildTreeTest(self, root: List[TreeNode]) -> Dict[int, TreeNode]:
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

class OptSolution:
    def isValidBSTInorderIterative(self, root: Optional[TreeNode]) -> bool:
        stack = [] #Store the next element to check
        prev_val = -math.inf
        root_ptr = root #Store the current element to check
        while stack or root_ptr:
            # Inorder Traversal
            while root_ptr:
                stack.append(root_ptr)
                root_ptr = root_ptr.left
            
            cur_root = stack.pop()

            #Check validation
            if cur_root is None:
                continue

            if cur_root.val <= prev_val:
                return False

            # Update and check next node
            prev_val = cur_root.val
            root_ptr = cur_root.right
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Inorder Traversal Check | Time: O(n) | Space: O(n)
        # Where n is the size of nodes in the Binary Tree

        # Iterative
        return self.isValidBSTInorderIterative(root)




