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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # LinkedList Traversal | Time: O(n+m) | Space: O(1),
        # n is the number of nodes in list1.
        # m is the number of nodes in list2.

        #Step0. Return None if both heads are None.
        if list1 is None and list2 is None: return None

        #Step1. Return list1 if list2 head is None.
        if list2 is None : return list1

        #Step2. Return list2 if list1 head is None.
        if list1 is None : return list2

        #Step3. Use two pointers: ptr1 and ptr2 to traverse both lists and merge by comparing each node.
        ptr1      = list1
        ptr1_prev = None
        ptr2      = list2
        ptr2_prev = None
        new_head  = None
        while ptr1 != None and ptr2 != None:
            if ptr1.val < ptr2.val:
                ptr1_nxt_tmp = ptr1.next
                ptr1.next = ptr2
                if ptr2_prev is not None:
                    ptr2_prev.next = ptr1
                else:
                    if ptr1_prev is None:
                        new_head = ptr1
                ptr2_prev = ptr1
                ptr1 = ptr1_nxt_tmp
                ptr1_prev = None
            else:
                ptr2_nxt_tmp = ptr2.next
                ptr2.next = ptr1
                if ptr1_prev is not None:
                    ptr1_prev.next = ptr2
                else:
                    if ptr2_prev is None:
                        new_head = ptr2
                ptr1_prev = ptr2
                ptr2 = ptr2_nxt_tmp
                ptr2_prev = None
        return new_head

class OptSolution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # LinkedList Traversal | Time: O(n+m) | Space: O(1),
        # n is the number of nodes in list1.
        # m is the number of nodes in list2.

        #Step0. Return None if both heads are None.
        if list1 is None and list2 is None: return None

        #Step1. Return list1 if list2 head is None.
        if list2 is None : return list1

        #Step2. Return list2 if list1 head is None.
        if list1 is None : return list2

        #Step3. Use two pointers: ptr1 and ptr2 to traverse both lists and merge by comparing each node.
        ptr1           = list1
        ptr2           = list2
        cur_trav_node  = ListNode(-1)
        new_head       = cur_trav_node
        while ptr1 != None and ptr2 != None:
            if ptr1.val < ptr2.val:
                cur_trav_node.next = ptr1
                ptr1 = ptr1.next
            else:
                cur_trav_node.next = ptr2
                ptr2 = ptr2.next
            cur_trav_node = cur_trav_node.next

        cur_trav_node.next = ptr1 if ptr1 else ptr2
        return new_head.next


