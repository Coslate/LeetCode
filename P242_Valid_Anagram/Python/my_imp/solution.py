from typing import Optional, List, Tuple, Dict, Deque, Set, Self
from collections import Counter
import math
from numpy.linalg import matrix_power
import numpy as np
import heapq

from collections import deque

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # String | Frequency Counter | Time: O(n+m) | Space: O(C),
        # Where n is the size of s.
        # Where m is the size of t.
        # Where C is the number of possible English letters, e.g.26

        #Step0. Return False if length of s does not equal to length of t.
        if len(s) != len(t): return False

        #Step1. Construct a freq counter and initialzie to 0.
        freq = {x:0 for x in 'abcdefghijklmnopqrstuvwxyz'}

        #Step2. Iterate over s, increment each encountered character in freq.
        for char in s:
            freq[char] += 1

        #Step3. Iterate overt, decrement each encountered character in freq.
        for char in t:
            freq[char] -= 1

        #Step4. Check each number of element in freq. If the number is negative, than return False.
        for c, num in freq.items():
            if num < 0:
                return False

        return True

class OptSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        pass


