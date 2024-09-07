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
    
    def serializeTree(self, root: Optional[TreeNode], serialized_tree: List[str]) -> None:
        if root is None:
            serialized_tree.append("#")
            return serialized_tree

        serialized_tree.append("^")
        serialized_tree.append(str(root.val))
        self.serializeTree(root.left, serialized_tree)
        self.serializeTree(root.right, serialized_tree)

    def genNext(self, patt: str) -> List[int]:
        patt_len = len(patt)
        next = [-1]*patt_len

        i = 1
        while i < patt_len:
            prev_match_loc = next[i-1]
            while patt[prev_match_loc+1] != patt[i] and prev_match_loc >= 0:
                prev_match_loc = next[prev_match_loc]
            if patt[prev_match_loc+1] == patt[i]:
                next[i] = prev_match_loc+1
            else:
                next[i] = -1
            i += 1

        return next

    def kmp(self, haystack: str, needle: str) -> int:
        target_len = len(haystack)
        patt_len   = len(needle)

        # generate next[] for efficiently resuming comparison
        next = self.genNext(needle)

        # compare haystack with needle
        pos_i = 0
        pos_j = 0
        while pos_i < target_len and pos_j < patt_len:
            if haystack[pos_i] == needle[pos_j]:
                pos_i += 1
                pos_j += 1
            elif pos_j == 0: # first match fails
                pos_i += 1
            else: # middle match fails
                pos_j = next[pos_j-1]+1

        if pos_j >= patt_len:
            return pos_i - pos_j
        else:
            return -1

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Iterative Traversing | O(n) | O(n)
        # Where n is the size of nodes in the Binary Tree.        
        serialized_root_tree_list = []
        serialized_sub_tree_list = []
        self.serializeTree(root, serialized_root_tree_list)
        self.serializeTree(subRoot, serialized_sub_tree_list)
        serialized_root_tree_str = "".join(serialized_root_tree_list)
        serialized_sub_tree_str = "".join(serialized_sub_tree_list)
        return self.kmp(serialized_root_tree_str, serialized_sub_tree_str) != -1

class OptSolution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:        
        # Iterative Traversing | O(n) | O(n)
        # Where n is the size of nodes in the Binary Tree.
        pass




