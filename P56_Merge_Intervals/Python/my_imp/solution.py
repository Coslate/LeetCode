from typing import Optional, List, Tuple, Dict, Deque, Set
import math
from numpy.linalg import matrix_power
import numpy as np

from collections import deque

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Linear Search | Time: O(nlogn) | Space: O(n), n is the number of input intervals.

        res = []
        intervals.sort()
        for interval in intervals:
            if len(res) == 0 or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
                res[-1][0] = min(res[-1][0], interval[0])

        return res

class OptSolution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pass


