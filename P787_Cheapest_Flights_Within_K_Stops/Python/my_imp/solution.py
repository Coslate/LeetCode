from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import defaultdict
import math
import numpy as np
import heapq
import random

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:    
        # Time: O(k*(E+n)) | Space: O(n)
        # Where k is the number of stops in the shortest path, and E is the number of edges in flights.
        # https://leetcode.com/problems/cheapest-flights-within-k-stops/editorial/?envType=problem-list-v2&envId=plakya4j

        MAX_DIST = 99*20000 # It is the possible maximum distance from src to dist, we can estimate as (n-1)*price = 99*10000, in order to set bigger to be deemed as 'non-reachable', I set it to 99*20000.

        shortest_dist = [MAX_DIST for _ in range(n)]
        shortest_dist[src] = 0
        for i in range(k+1):
            tmp = [_ for _ in shortest_dist]
            for edges in flights:
                if shortest_dist[edges[0]] != MAX_DIST:
                    tmp[edges[1]] = min(tmp[edges[1]], shortest_dist[edges[0]] + edges[2])
                
            shortest_dist = [_ for _ in tmp]

        return -1 if shortest_dist[dst] == MAX_DIST else shortest_dist[dst]