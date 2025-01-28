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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:    
        # Time: O(N) | Space: O(N)
        # Where N is the number of elements linked list
        # https://leetcode.com/problems/palindrome-linked-list/editorial/
        cur = head
        rev_head = None
        prev = None

        while cur:
            rev_node = ListNode(cur.val, prev)
            if cur.next == None:
                rev_head = rev_node
            prev = rev_node
            cur = cur.next

        cur = head
        rev_cur = rev_head
        while cur:
            if cur.val != rev_cur.val:
                return False
            cur = cur.next
            rev_cur = rev_cur.next

        return True
        