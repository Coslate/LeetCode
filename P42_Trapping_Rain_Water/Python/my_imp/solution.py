from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import Counter
import math
import numpy as np
import heapq

class Solution:
    def trap(self, height: List[int]) -> int:
        # Time: O(N) | Space: O(1)
        # Two Pointers
        # Where N is the number of elements in height.
        # https://leetcode.com/problems/trapping-rain-water/editorial/?envType=problem-list-v2&envId=plakya4j

        n = len(height)
        left_max = height[0] # max height from left to current left_ptr
        right_max = height[n-1] # max height from right to the current right_ptr
        left_ptr = 0
        right_ptr = n-1
        ans = 0
        while left_ptr < right_ptr:
            if left_max < right_max:
                left_ptr += 1
                left_max = max(left_max, height[left_ptr])
                ans += left_max - height[left_ptr]
            else:
                right_ptr -=1
                right_max = max(right_max, height[right_ptr])
                ans += right_max - height[right_ptr]

        return ans

    def trap_dynamic_programming(self, height: List[int]) -> int:
        # Time: O(N) | Space: O(N)
        # Dynamic Programming
        # Where N is the number of elements in height.
        # https://leetcode.com/problems/trapping-rain-water/editorial/?envType=problem-list-v2&envId=plakya4j

        n = len(height)
        left_max = [0]*n
        right_max = [0]*n

        left_max[0] = height[0]
        right_max[n-1] = height[n-1]

        # Construct left_max[]
        for i in range(1, n-1):
            left_max[i] = max(left_max[i-1], height[i])

        # Construct right_max[]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        # Get final answer
        ans = 0
        for i in range(1, n-1):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans

