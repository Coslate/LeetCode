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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min Heap Extracting | Time: O(nlogk) | Space: O(n),
        # n is the number of nodes in all the lists.
        # k is the number of list in lists.

        #Step0. Return None if lists is None
        if lists is None: return None

        #Step1. Construct and initialize heap data structure.
        heap_dt = []
        for list_node in lists:
            if type(list_node) is list:
                if list_node[0] is not None: heapq.heappush(heap_dt, HeapNode(list_node[0]))
            else:
                if list_node is not None: heapq.heappush(heap_dt, HeapNode(list_node))

        #Step2. Initialize current_node pointed to a dummy node.
        current_node = ListNode(-1)
        prev_head    = current_node

        #Step3. Keep extracting min node among the front end nodes among k lists.
        while heap_dt:
            min_heap_node = heapq.heappop(heap_dt)
            min_node = min_heap_node.node
            current_node.next = min_node
            current_node = current_node.next
            if min_node and min_node.next:
                heapq.heappush(heap_dt, HeapNode(min_node.next))

        return prev_head.next

class OptSolution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Divide and Conquer | Time: O(nlogk) | Space: O(1),
        # n is the number of nodes in all the lists.
        # k is the number of list in lists.

        #Step0. Return None if lists is None
        if lists is None or len(lists) == 0: return None
        interval = 1
        length = len(lists)

        #Step1. Every two lists are merged using mergeTwoLists().
        #Step2. Return lists[0], storing the final merged result.
        if type(lists[0]) is list:
            while interval < length:
                for i in range(0, length-interval, interval*2):
                    lists[i][0] = self.mergeTwoLists(lists[i][0], lists[i+interval][0])

                interval *= 2
            return lists[0][0] if length > 0 else None
        else:
            while interval < length:
                for i in range(0, length-interval, interval*2):
                    lists[i] = self.mergeTwoLists(lists[i], lists[i+interval])

                interval *= 2
            return lists[0] if length > 0 else None

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


