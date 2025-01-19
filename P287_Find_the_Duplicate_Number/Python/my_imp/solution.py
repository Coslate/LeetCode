from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import Counter, deque
import math
import numpy as np
import heapq
import random

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Time: O(NlogN) | Space: O(1)
        # Where N is the number of elements in nums.
        # https://leetcode.com/problems/find-the-duplicate-number/editorial/?envType=problem-list-v2&envId=plakya4j

        low = 1
        high = len(nums)

        # Binary Search
        while low < high:
            mid = (low + high)//2
            count = sum((num<=mid) for num in nums)

            if count <= mid:
                low = mid + 1
            else:
                high = mid

        return high


