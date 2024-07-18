from typing import Optional, List, Tuple, Dict, Deque, Set
import math
from numpy.linalg import matrix_power
import numpy as np

from collections import deque

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Linear Search | Time: O(n) | Space: O(1), n is the number of input intervals.
        # As we only need an array for the output, so the Space could be O(1).

        #Step0. Return inserted newInterval list if input len of intervals is zero
        if len(intervals) == 0: return [newInterval]

        #Step1. Iterate all the interval that end points < start point of the inserting interval.
        res = []
        idx_n = 0

        while(idx_n < len(intervals) and intervals[idx_n][1] < newInterval[0]):
            res.append(intervals[idx_n])
            idx_n += 1

        #Step2. Merge the overlapping intervals.
        newInterval_tmp = [x for x in newInterval]
        new_start, new_end = newInterval[0], newInterval[1]
        while(idx_n < len(intervals) and intervals[idx_n][0] <= newInterval_tmp[1]):
            new_start = min(newInterval_tmp[0], intervals[idx_n][0])
            new_end   = max(newInterval_tmp[1], intervals[idx_n][1])
            newInterval_tmp = [new_start, new_end]
            idx_n += 1
        res.append([new_start, new_end])

        #Step3. Iterate all the interval that start points > end point of the inserting interval.
        while(idx_n < len(intervals) and intervals[idx_n][0] > newInterval_tmp[1]):
            res.append(intervals[idx_n])
            idx_n += 1

        return res

class OptSolution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # UnionFind | Time: O(V + E*alpha(V)) | Space: O(V).
        pass


