from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import Counter
import math
import numpy as np
import heapq
import random

class Node:
    def __init__(self, name='NA', val=None):
        self.name = name
        self.val = val

    def __lt__(self, other):
        return self.val < other.val

class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index: int) -> int:
        return (index-1)//2

    def _right_child(self, index: int) -> int:
        index_cal = index*2+2
        return index_cal if index_cal < len(self.heap) else None

    def _left_child(self, index: int) -> int:
        index_cal = index*2+1
        return index_cal if index_cal < len(self.heap) else None

    def _swap(self, index_i: int, index_j: int) -> None:
        self.heap[index_i], self.heap[index_j] = self.heap[index_j], self.heap[index_i]

    def _heapify_up(self, index: int) -> None:
        while index > 0 and self.heap[index].val < self.heap[self._parent(index)].val:
            self._swap(index, self._parent(index))
            index = self._parent(index)
    
    def _heapify_down(self, index: int) -> None:
        cur_index = index

        while cur_index < len(self.heap):
            right_child_index = self._right_child(cur_index)
            left_child_index = self._left_child(cur_index)
            smallest_child_index = None

            if right_child_index is not None and left_child_index is not None :
                if self.heap[right_child_index].val > self.heap[left_child_index].val:
                    smallest_child_index = left_child_index
                else:
                    smallest_child_index = right_child_index
            elif right_child_index is not None:
                smallest_child_index = right_child_index
            elif left_child_index is not None:
                smallest_child_index = left_child_index

            if smallest_child_index is not None and self.heap[smallest_child_index].val < self.heap[cur_index].val:
                self._swap(smallest_child_index, cur_index)
                cur_index = smallest_child_index
            else:
                break

    def insert(self, element: Node) -> None:
        self.heap.append(element)
        self._heapify_up(len(self.heap)-1)

    def extract_min(self) -> Node:
        if len(self.heap) == 0:
            raise IndexError('Heap is empty.')
        if len(self.heap) == 1:
            return self.heap.pop()

        min_ele = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return min_ele

    def get_min(self) -> Node:
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            raise IndexError('Heap is empty.')

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Time: O(NlogM) | Space: O(1)
        # Binary Search
        # Where N is the number of piles in piles[].
        # M is the number of max(piles)
        # https://leetcode.com/problems/koko-eating-bananas/editorial/?envType=problem-list-v2&envId=plakya4j

        left = 1
        right = max(piles)

        while left < right:
            mid = (left+right)//2

            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(pile/mid)

            if hours_spent > h:
                left = mid+1
            else: #hours_spent <= h
                right = mid

        return right
