from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
import collections
import math
import numpy as np
import heapq

char = TypeVar("char", bound=str)

class Trie:
    class TrieNode:
        def __init__(self):
            self._children= {}
            self._isEnd = False
        
        @property
        def isEnd(self) -> bool:
            return self._isEnd
        
        @property
        def children(self) -> Dict[char, 'TrieNode']:
            return self._children

        @isEnd.setter
        def isEnd(self, value: bool) -> None:
            self._isEnd = value

        def put(self, ch: char, node: 'TrieNode') -> None:
            self._children[ch] = node

        def get(self, ch: char) -> 'TrieNode':
            return self._children[ch]
        
        def containsKey(self, ch: char) -> bool:
            return True if ch in self._children else False


    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if not node.containsKey(word[i]):
                node.put(word[i], self.TrieNode())
            node = node.get(word[i])
        node.isEnd = True
        
    def searchPrefix(self, word: str) -> Optional[TrieNode]:
        node = self.root
        for i in range(len(word)):
            if node.containsKey(word[i]):
                node = node.get(word[i])
            else:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd == True

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return node is not None

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Inorder Traversal Check | Time: O(n) | Space: O(n)
        # Where n is the size of nodes in the Binary Tree
        pass





