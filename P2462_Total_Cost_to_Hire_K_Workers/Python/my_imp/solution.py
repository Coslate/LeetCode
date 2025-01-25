from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import defaultdict
import math
import numpy as np
import heapq
import random

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:    
        # Time: O(M + KlogM)) | Space: O(M)
        # Where M is the number of candidates, and K is k.
        # https://leetcode.com/problems/total-cost-to-hire-k-workers/editorial/

        head_list = costs[:candidates]
        tail_list = costs[max(candidates, len(costs)-candidates):]
        heapq.heapify(head_list)
        heapq.heapify(tail_list)

        next_head = candidates
        next_tail = len(costs) - 1 - candidates
        ans = 0

        for _ in range(k):
            if not tail_list or head_list and head_list[0] <= tail_list[0]:
                ans += heapq.heappop(head_list)

                if next_head <= next_tail:
                    heapq.heappush(head_list, costs[next_head])
                    next_head += 1
            else:
                ans += heapq.heappop(tail_list)

                if next_head <= next_tail:
                    heapq.heappush(tail_list, costs[next_tail])
                    next_tail -= 1

        return ans
