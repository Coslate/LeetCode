from typing import Optional, List, Tuple, Dict, Deque, Set, Self
import math
from numpy.linalg import matrix_power
import numpy as np
import heapq

from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class HeapNode:
    def __init__(self, node=Optional[ListNode]):
        self.node = node

    def __lt__(self, others=Optional[Self]):
        return self.node.val < others.node.val

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Middle Search + Reverse Linked List + Merged Linked List | Time: O(n) | Space: O(1),
        # n is the number of nodes in all the lists.

        #Step0. Return None if head is None
        if head is None: return None

        #Step1. Find the middle point of the original list
        slow_ptr = head
        fast_ptr = head
        middle_ptr = head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        middle_ptr = slow_ptr

        #Step2. Reverse the second part of the original list starting from middle point.
        #       Convert 1 -> 2 -> 3 -> 4 -> 5 -> 6 to 1 -> 2 -> 3 -> 4 and 6 -> 5 -> 4.
        #       4 is repeated, and it is redundant in first list.
        prev_node = None
        current_node = middle_ptr
        second_head = None
        while current_node:
            tmp_nxt_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = tmp_nxt_node
        second_head = prev_node

        #Step3. Merge two lists. As for implementation trick, the second list mus shorter than the first list.
        #       The last element in the first list is redundant.
        first_ptr = head
        second_ptr = second_head
        while second_ptr != None:
            first_tmp_nxt  = first_ptr.next
            second_tmp_nxt = second_ptr.next
            first_ptr.next = second_ptr
            second_ptr.next = first_tmp_nxt
            first_ptr = first_tmp_nxt
            second_ptr = second_tmp_nxt
        if first_ptr != None:
            first_ptr.next = None


class OptSolution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pass


