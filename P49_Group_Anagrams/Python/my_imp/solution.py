from typing import Optional, List, Tuple, Dict, Deque, Set, Self
import collections
import math
from numpy.linalg import matrix_power
import numpy as np
import heapq


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # String | Frequency Counter | Time: O(kn) | Space: O(kn),
        # k is the maximum length of string in strs.
        # n is the length of strs.

        #Step0. Declare ans as mapping from counter to list of string in strs.
        ans: typing.DefaultDict[Tuple[int], List[str]] = collections.defaultdict(list)

        #Step1. Iterate over strs to categorize each string into right key.
        for string in strs:
            counter = [0]*26
            for char in string:
                counter[ord(char) - ord('a')] += 1

            ans[tuple(counter)].append(string)
        return ans.values()

class OptSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # String | Frequency Counter | Time: O(n+m) | Space: O(C),
        pass


