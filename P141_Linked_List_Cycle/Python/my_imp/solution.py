from typing import Optional, List, Tuple, Dict, Deque, Set
import math
from numpy.linalg import matrix_power
import numpy as np
import heapq

from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # LinkedList Traversal + Hash | Time: O(n) | Space: O(n),
        # n is the number of nodes in linked list.

        #Step0. Return None if head is None.
        if head is None: return None

        #Step1. Traverse the whole list, store seen node in a hash.
        nodes_seen = set()
        cur_node = head
        while cur_node:
            if cur_node not in nodes_seen:
                nodes_seen.add(cur_node)
            else:
                return True
            cur_node = cur_node.next
        return False

class OptSolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # LinkedList Traversal + Two Pointers | Time: O(n) | Space: O(1),
        # n is the number of nodes in linked list.

        #Step0. Return None if head is None.
        if head is None: return None

        #Step1. Set slow_ptrs, fast_ptrs.
        slow_ptrs = head
        fast_ptrs = head.next

        while slow_ptrs != fast_ptrs:
            if fast_ptrs is not None and fast_ptrs.next is not None:
                slow_ptrs = slow_ptrs.next
                fast_ptrs = fast_ptrs.next.next
            else:
                return False
        return True

