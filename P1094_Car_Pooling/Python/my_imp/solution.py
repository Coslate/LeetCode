from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import defaultdict
import math
import numpy as np
import heapq
import random

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:    
        # Time: O(NlogN)) | Space: O(N)
        # Where N is the number of list in points.
        # The sorting in python is Timsort, having space complexity of O(n). Besides, we need O(n) for time_stamp[]
        # https://leetcode.com/problems/car-pooling/editorial/

        time_stamp = []
        for trip in trips:
            time_stamp.append((trip[1], trip[0]))
            time_stamp.append((trip[2], -trip[0]))

        time_stamp.sort()
        accumulate_passenger = 0

        for time, passenger_change in time_stamp:
            accumulate_passenger += passenger_change
            if accumulate_passenger > capacity:
                return False

        return True