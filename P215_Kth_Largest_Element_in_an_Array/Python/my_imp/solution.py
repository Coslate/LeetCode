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
    def findKthLargest(self, nums: List[int], k: int) -> int:    
        # Time: O(Nlogk) | Space: O(k)
        # MinHeap
        # Where N is the number of elements in nums.
        # https://leetcode.com/problems/kth-largest-element-in-an-array/editorial/?envType=problem-list-v2&envId=plakya4j

        '''
        # My own MinHeap()
        min_heap = MinHeap()
        count = 0
        for num in nums:
            if min_heap.size() == k:
                min_heap.insert(Node(str(num), num))
                min_heap.extract_min()
            else:
                min_heap.insert(Node(str(num), num))

        return min_heap.extract_min().val
        '''

        # Lib heapq implementation
        min_heap = []
        count = 0
        for num in nums:
            if len(min_heap) == k:
                heapq.heappush(min_heap, Node(str(num), num))
                heapq.heappop(min_heap)
            else:
                heapq.heappush(min_heap, Node(str(num), num))

        return min_heap[0].val


    def findKthLargestQuickSelect(self, nums: List[int], k: int) -> int:
        # Time: O(N), T(N) = T(N/2)+O(N) | Space: O(N)
        # QuickSelect
        # Where N is the number of elements in nums.
        # https://leetcode.com/problems/kth-largest-element-in-an-array/editorial/?envType=problem-list-v2&envId=plakya4j

        pivot = random.randint(0, len(nums)-1)
        left = []
        right = []
        mid = []
        for num in nums:
            if num > nums[pivot]:
                left.append(num)
            elif num < nums[pivot]:
                right.append(num)
            else:
                mid.append(num) 

        if k <= len(left):
            return self.findKthLargestQuickSelect(left, k)
        
        if len(left) + len(mid) < k:
            return self.findKthLargestQuickSelect(right, k-len(left)-len(mid))

        return nums[pivot]

