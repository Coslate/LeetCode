from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import Counter, deque
import math
import numpy as np
import heapq
import random

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:        
        # Time: O(Nlogk) = O(Nlog26) = O(N) | Space: O(26) = O(1)
        # Max Heap
        # Where N is the number of task in tasks[].
        # https://leetcode.com/problems/n-queens/editorial/?envType=problem-list-v2&envId=plakya4j

        # Calculate the number of task and corresponding freq.
        freq = [0]*26
        for character in tasks:
            freq[ord(character) - ord('A')] += 1

        # Build max heap
        max_heap = [-x for x in freq if x > 0]
        heapq.heapify(max_heap)

        ans_time = 0
        while max_heap:
            cool_cycle = n + 1
            task_count = 0
            need_store = []
            while max_heap and cool_cycle > 0:
                curr_task_freq = -heapq.heappop(max_heap)
                if curr_task_freq > 1:
                    need_store.append(-(curr_task_freq-1))
                task_count += 1
                cool_cycle -= 1

            for upd_freq in need_store:
                heapq.heappush(max_heap, upd_freq)

            ans_time += task_count if not max_heap else n+1
        
        return ans_time

            


            

            



