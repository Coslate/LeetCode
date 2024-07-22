from typing import Optional, List, Tuple, Dict, Deque, Set
import math
from numpy.linalg import matrix_power
import numpy as np
import heapq

from collections import deque

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Sorted | Time: O(nlogn) | Space: O(n), n is the number of input intervals.

        #Step0. Return 0 if intervals[] is empty.
        if not intervals: return 0

        #Step1. Sort according to the start points.
        intervals.sort(key=lambda x:x[0])

        #Step2. Construct a min-heap data structure to track the end point of meeting rooms.
        room_resource_heap = []

        #Step3. Add the first room.
        heapq.heappush(room_resource_heap, intervals[0][1])

        #Step4. Iterate all the rest of the intervals, if there is an available room, replace the
        #       end point with the new one.
        for meet_time in intervals[1:]:
            if meet_time[0] >= room_resource_heap[0]:
                heapq.heappop(room_resource_heap)

            heapq.heappush(room_resource_heap, meet_time[1])

        return len(room_resource_heap)

class OptSolution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pass


