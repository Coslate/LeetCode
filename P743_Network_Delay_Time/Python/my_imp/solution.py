from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import defaultdict
import math
import numpy as np
import heapq
import random

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:    
        # Time: O(E+N+ElogE) | Space: O(N+E)
        # Where N is n, and E is the number of edges in times, and E = N^2, so Time could be O(N^2logN), and Space could be O(N^2).
        # https://leetcode.com/problems/network-delay-time/editorial/?envType=problem-list-v2&envId=plakya4j
        adj_list = defaultdict(list)
        for edges in times:
            adj_list[edges[0]].append([edges[1], edges[2]])
        
        time_to_dst = [math.inf for _ in range(n+1)]

        def dijkstra(adj_list: {}, src: int, times: List[List[int]], time_to_dst: []) -> None:
            time_to_dst[src] = 0
            pq = []
            heapq.heappush(pq, (0, src))

            while pq:
                cur_dst, cur_node = heapq.heappop(pq)

                for neighbor in adj_list[cur_node]:
                    n_node = neighbor[0]
                    n_cost = neighbor[1]
                    if time_to_dst[cur_node] + n_cost < time_to_dst[n_node]:
                        time_to_dst[n_node] = time_to_dst[cur_node] + n_cost
                        heapq.heappush(pq, (time_to_dst[n_node], n_node))

        dijkstra(adj_list, k, times, time_to_dst)
        max_dealy_time = -1
        for i in range(1, n+1):
            max_dealy_time = max(max_dealy_time, time_to_dst[i])
        
        return -1 if max_dealy_time == math.inf else max_dealy_time