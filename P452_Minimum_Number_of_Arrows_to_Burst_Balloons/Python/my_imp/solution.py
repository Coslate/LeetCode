from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import defaultdict
import math
import numpy as np
import heapq
import random

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:    
        # Time: O(NlogN)) | Space: O(N)
        # Where N is the number of list in points.
        # The sorting in python is Timsort, having space complexity of O(n)
        # https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

        # Sorting
        points.sort(key = lambda x: x[1])

        # Greedy
        arrow_end = points[0][1]
        arrow = 1
        for index in range(1, len(points)):
            x_start, x_end = points[index]
            if arrow_end < x_start:
                arrow += 1
                arrow_end = x_end

        return arrow

