from typing import Optional, List, Tuple, Dict, Deque, Set
import math
from numpy.linalg import matrix_power
import numpy as np

from collections import deque

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sorted | Time: O(nlogn) | Space: O(n), n is the number of input intervals.

        #Step0. Sort according to the start points.
        sorted_intervals = sorted(intervals, key=lambda x:x[0])

        #Step1. Iterate each intervals to make sure each end point is smaller than next start point.
        index = 1
        for meeting_time in sorted_intervals[1:]:
            if meeting_time[0] >= sorted_intervals[index-1][1]:
                index += 1
                continue
            else:
                return False

        return True

class OptSolution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        pass


