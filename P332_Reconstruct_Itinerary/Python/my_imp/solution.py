from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import defaultdict
import math
import numpy as np
import heapq
import random

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:    
        # Time: O(ElogE) | Space: O(E)
        # Graph DFS
        # Where E = len(tickets)
        # https://leetcode.com/problems/reconstruct-itinerary/solutions/6280175/video-visualized-solution-python-javascript-java-c/?envType=problem-list-v2&envId=plakya4j

        # Build the graph
        adj_list = defaultdict(list)
        for dep, arv in sorted(tickets, reverse=True): #in reverse order to first explore small lexical order
            adj_list[dep].append(arv)

        # Traverse from small lexical order
        st = ['JFK']
        itenary = []
        while st:
            if adj_list[st[-1]]:
                st.append(adj_list[st[-1]].pop())
            else:
                itenary.append(st.pop())

        return itenary[::-1]




