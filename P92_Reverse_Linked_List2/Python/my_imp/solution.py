from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import defaultdict
import math
import numpy as np
import heapq
import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:    
        # Time: O(N)) | Space: O(1)
        # Where N is the number of elements in the linked list head[].
        # https://leetcode.com/problems/reverse-linked-list-ii/editorial/

        m = left
        n = right

        prev, cur = None, head
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m-1, n-1
        
        tail = cur
        prev_tail = prev

        while n > 0:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            n -= 1

        if prev_tail:
            prev_tail.next = prev
        else:
            head = prev

        tail.next = cur
        return head