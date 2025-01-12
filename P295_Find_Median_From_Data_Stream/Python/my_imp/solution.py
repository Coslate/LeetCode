from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import Counter
import math
import numpy as np
import heapq

class Node:
    def __init__(self, name='NA', val=None):
        self.name = name
        self.val = val

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

class MaxHeap:
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
        while index > 0 and self.heap[index].val > self.heap[self._parent(index)].val:
            self._swap(index, self._parent(index))
            index = self._parent(index)
    
    def _heapify_down(self, index: int) -> None:
        cur_index = index

        while cur_index < len(self.heap):
            right_child_index = self._right_child(cur_index)
            left_child_index = self._left_child(cur_index)
            largest_child_index = None

            if right_child_index is not None and left_child_index is not None :
                if self.heap[right_child_index].val < self.heap[left_child_index].val:
                    largest_child_index = left_child_index
                else:
                    largest_child_index = right_child_index
            elif right_child_index is not None:
                largest_child_index = right_child_index
            elif left_child_index is not None:
                largest_child_index = left_child_index

            if largest_child_index is not None and self.heap[largest_child_index].val > self.heap[cur_index].val:
                self._swap(largest_child_index, cur_index)
                cur_index = largest_child_index
            else:
                break

    def insert(self, element: Node) -> None:
        self.heap.append(element)
        self._heapify_up(len(self.heap)-1)

    def extract_max(self) -> Node:
        if len(self.heap) == 0:
            raise IndexError('Heap is empty.')
        if len(self.heap) == 1:
            return self.heap.pop()

        max_ele = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return max_ele

    def get_max(self) -> Node:
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            raise IndexError('Heap is empty.')

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

class MedianFinder:
    def __init__(self):
        self.lo = MaxHeap()
        self.hi = MinHeap()
        

    def addNum(self, num: int) -> None:
        self.lo.insert(Node(str(num), num))
        self.hi.insert(self.lo.extract_max())
        if self.lo.size() < self.hi.size() :
            self.lo.insert(self.hi.extract_min())

    def findMedian(self) -> float:
        # Time: O(logN) | Space: O(N)
        # Where N is the number of elements in streams.
        # https://leetcode.com/problems/find-median-from-data-stream/        
        if self.lo.size() == 0: return None
        return self.lo.get_max().val if self.lo.size() != self.hi.size() else (self.lo.get_max().val + self.hi.get_min().val)/2

    # Your MedianFinder object will be instantiated and called as such:
    # obj = MedianFinder()
    # obj.addNum(num)
    # param_2 = obj.findMedian()    




        