from typing import Optional, List, Tuple, Dict, Deque, Set, Self
from collections import Counter
import math
from numpy.linalg import matrix_power
import numpy as np
import heapq

from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Sliding Window | Time: O(n+m) | Space: O(n+m),
        # Where n is the size of s.
        # Where m is the size of t.

        #Step0. Return None if s is None
        if s is None: return None

        #Step1. Return s[0] if t is None
        if t is None: return s[0]

        #Step2. Initialize the required variables.
        dict_t = Counter(t)
        required = len(dict_t)

        #Step3. Iterate over the s.
        left = 0
        right = 0
        freq  = {}
        formed = 0
        smallest_len = float('inf')
        smallest_s   = ''
        while right < len(s):
            char = s[right]
            freq[char] = freq.get(char, 0) + 1

            if char in dict_t and freq[char] == dict_t[char]:
                formed += 1

            while left <= right and formed == required :
                #Save the smallest window size until now.
                sub_len = right-left+1
                if sub_len < smallest_len:
                    smallest_len = sub_len
                    smallest_s = s[left:right+1]

                #Try to minimize the window size
                remove_char = s[left]
                freq[remove_char] -= 1
                if remove_char in dict_t and freq[remove_char] < dict_t[remove_char]:
                    formed -= 1
                left += 1

            right += 1

        return smallest_s


class OptSolution:
    def minWindow(self, s: str, t: str) -> str:
        # Sliding Window | Time: O(n+m) | Space: O(n+m),
        # Where n is the size of s.
        # Where m is the size of t.

        #Step0. Return None if s is None
        if s is None: return None

        #Step1. Return s[0] if t is None
        if t is None: return s[0]

        #Step2. Initialize the required variables.
        dict_t = Counter(t)
        required = len(dict_t)

        #Step3. Generate flittered s, contianing all the character in t.
        flittered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                flittered_s.append((i, char))

        #Step3. Iterate over the flittered_s.
        left = 0
        right = 0
        freq  = {}
        formed = 0
        smallest_len = float('inf')
        smallest_s   = ''
        while right < len(flittered_s):
            char = flittered_s[right][1]
            freq[char] = freq.get(char, 0) + 1

            if freq[char] == dict_t[char]:
                formed += 1

            while left <= right and formed == required :
                #Save the smallest window size until now.
                end = flittered_s[right][0]
                start = flittered_s[left][0]
                sub_len = end-start+1
                if sub_len < smallest_len:
                    smallest_len = sub_len
                    smallest_s = s[start:end+1]

                #Try to minimize the window size
                remove_char = flittered_s[left][1]
                freq[remove_char] -= 1
                if freq[remove_char] < dict_t[remove_char]:
                    formed -= 1
                left += 1

            right += 1

        return smallest_s




