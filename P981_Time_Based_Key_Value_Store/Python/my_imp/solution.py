from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import Counter, deque
import math
import numpy as np
import heapq
import random

class TimeMap:
    def __init__(self):
        self.key_value_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Time: O(ML) | Space: O(ML)
        # Where M is the number of set() call, and L is the length of key str.
        # Each set() call takes O(L) to convert key string into a hash value.
        # https://leetcode.com/problems/time-based-key-value-store/editorial/?envType=problem-list-v2&envId=plakya4j

        if key in self.key_value_store:
            self.key_value_store[key].append([timestamp, value])
        else:
            self.key_value_store[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        # Time: O(N*(L+log(M))) | Space: O(1)
        # Where N is the number of get() call, and L is the length of key str, M is the length of the selected key bucket.
        # Each get() call takes O(L+log(M)) to to binary search.
        # Each search in binary search takes O(L) to convert key to hash value, and O(logM) to search.
        # https://leetcode.com/problems/time-based-key-value-store/editorial/?envType=problem-list-v2&envId=plakya4j

        if not self.key_value_store:
            return ''

        if not key in self.key_value_store:
            return ''

        if timestamp < self.key_value_store[key][0][0]:
            return ''

        # Binary Search
        left = 0
        right = len(self.key_value_store[key])

        # Readuce seach time from O(L*log(M)) to O(L+log(M))
        search_bucket = self.key_value_store[key]

        while left < right:
            mid = (left + right)//2

            if search_bucket[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        return '' if right == 0 else self.key_value_store[key][right-1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

