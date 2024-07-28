from typing import Optional, List, Tuple, Dict, Deque, Set, Self
import math
from numpy.linalg import matrix_power
import numpy as np
import heapq

from collections import deque

class Solution:
    def canMakeValidSubstring(self, s: str, k: int, valid_len: int) -> bool:
        freq = {}
        max_freq = -1
        start = 0

        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1
            sub_str_len = end-start+1

            if sub_str_len > valid_len:
                freq[s[start]] -= 1
                start += 1

            max_freq = max(freq[s[end]], max_freq)
            if valid_len - max_freq <= k:
                return True
        return False

    def characterReplacement(self, s: str, k: int) -> int:
        # Binary Search + Sliding Window | Time: O(nlogn) | Space: O(m),
        # n is the number of elements in s.
        # m is the number of possible chars in s. e.g. m = 26.

        #Step0. Return 0 if s is None
        if s is None: return 0

        #Step1. Binary Search to find the max length of valid substring.
        #Step2. Use sliding window with formula: valid_len-max_freq <= k to check if a substring with specific len
        #       does exist.
        left_ptr = 0
        right_ptr = len(s)+1
        while left_ptr + 1 < right_ptr:
            mid_ptr = (left_ptr + right_ptr)//2
            if self.canMakeValidSubstring(s, k, mid_ptr):
                left_ptr = mid_ptr
            else:
                right_ptr = mid_ptr

        return left_ptr

class OptSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding Window | Time: O(n) | Space: O(m),
        # n is the number of elements in s.
        # m is the number of possible chars in s. e.g. m = 26.

        #Step0. Return 0 if s is None
        if s is None: return 0

        #Step1. Iterate all the possible end position in range(len(s))
        #Step2. In each loop, check if substring is valid, if valid -> enlarge the substring,
        #       else move toward right.
        start = 0
        end   = 0
        max_freq = -1
        max_valid_len = 0
        freq = {}

        while end < len(s):
            freq[s[end]] = freq.get(s[end], 0) + 1
            max_freq = max(max_freq, freq[s[end]])
            sub_str_len = end-start+1
            if sub_str_len-max_freq <= k:
                end += 1
                max_valid_len = max(max_valid_len, sub_str_len)
            else:
                end += 1
                freq[s[start]] -= 1
                start += 1

        return max_valid_len



