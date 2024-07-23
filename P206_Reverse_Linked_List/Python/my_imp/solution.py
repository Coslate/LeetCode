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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Sorted | Time: O(n) | Space: O(1), n is the number of nodes in linked
        # list.

        #Step0. Return None if head is None.
        if head is None: return None

        #Step1. Traverse the whole list, store previous node, and reverse the 'next' direction.
        cur_node = head
        prev_node = None
        while(cur_node != None):
            orig_next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = orig_next_node

        head = prev_node
        return head

class OptSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


