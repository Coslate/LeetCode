from typing import Optional, List, Tuple, Dict, Deque, Set
import math
from numpy.linalg import matrix_power
import numpy as np

from collections import deque

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Linear Search | Time: O(nlogn) | Space: O(n), n is the number of input intervals.

        #Step0. Sort according to the end points.
        sorted_intervals = sorted(intervals, key = lambda x: x[1])

        #Step1. Set the earliest end pt k to the end pt of the first sorted element.
        k = sorted_intervals[0][1]

        #Step2. Iterated over the sorted arrays:
        #       a. If the current start point is larger than k, k = end point
        #          of the current element.
        #       b. If the current start point is smaller or eaqual to k, drop
        #          the element and continue, and k is unchanged.
        count = 0
        for x in sorted_intervals[1:]:
            if x[0] >= k:
                k = x[1]
            else:
                count += 1

        return count

class OptSolution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        pass


