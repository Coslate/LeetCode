from typing import Optional, List, Tuple, Dict, Deque, Set, Self
from collections import Counter, deque
import math
import heapq

class Solution:
    def genNext(self, patt: str) -> List[int]:
        patt_len = len(patt)
        next = [-1]*patt_len

        i = 1
        while i < patt_len:
            prev_match_loc = next[i-1]
            while patt[prev_match_loc+1] != patt[i] and prev_match_loc >= 0:
                prev_match_loc = next[prev_match_loc]
            if patt[prev_match_loc+1] == patt[i]:
                next[i] = prev_match_loc+1
            else:
                next[i] = -1
            i += 1

        return next

    def kmp(self, haystack: str, needle: str) -> int:
        target_len = len(haystack)
        patt_len   = len(needle)

        # generate next[] for efficiently resuming comparison
        next = self.genNext(needle)

        # compare haystack with needle
        pos_i = 0
        pos_j = 0
        while pos_i < target_len and pos_j < patt_len:
            if haystack[pos_i] == needle[pos_j]:
                pos_i += 1
                pos_j += 1
            elif pos_j == 0: # first match fails
                pos_i += 1
            else: # middle match fails
                pos_j = next[pos_j-1]+1

        if pos_j >= patt_len:
            return pos_i - pos_j
        else:
            return -1

    def strStr(self, haystack: str, needle: str) -> int:
        # String | KMP | Time: O(n+m) | Space: O(n+m),
        # Where n is the length of haystack (targed string).
        # Where m is the length of needle (pattern string).
        return self.kmp(haystack, needle)

class OptSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        pass


