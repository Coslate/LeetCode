from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import defaultdict
import math
import numpy as np
import heapq
import random

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right        

class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:    
        # Time: O(logN) | Space: O(logN)
        # Where N is the number of elements in the Binary Tree.
        # https://leetcode.com/problems/binary-tree-upside-down/solutions/49444/8-line-recursive-python/

        if not root or ((not root.left) and (not root.right)):
            return root

        left = self.upsideDownBinaryTree(root.left)
        root.left.right = root
        root.left.left = root.right
        root.left = None
        root.right = None
        return left
