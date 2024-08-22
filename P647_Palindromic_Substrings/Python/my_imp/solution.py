from typing import Optional, List, Tuple, Dict, Deque, Set, Self
import collections
import math
from numpy.linalg import matrix_power
import numpy as np
import heapq


class Solution:
    def countSubstrings(self, s: str) -> int:
        # Dynamic Programming | Time: O(n) | Space: O(n),
        # Where n is the size of input s.

        #Step0. If s is empty, return 0
        if not s: return 0

        #Step1. Initialize dp[i][j] = false. dp[i][j] means if s[i:j+1]is valid palindrome.
        dp = [[False]*len(s) for i in range(len(s))]

        #Step2. Initialize base cases: a. each single char, b. two cintinuous chars.
        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s)):
            j = i+1
            if j > len(s)-1:
                break
            else:
                if s[i] == s[j]:
                    dp[i][j] = True

        #Step3. Optimized substructure: dp[i][j] is true only if dp[i+1][j-1] is true and s[i]==s[j].
        for length in range(3, len(s)+1):
            for i in range(len(s)-length+1):
                j = i+length-1
                dp[i][j] = dp[i+1][j-1] and s[i]==s[j]

        #Step4. Count the number of true lements in dp.
        ans = 0
        for i in range(len(s)):
            ans += sum(dp[i])

        return ans

class OptSolution:
    def countSubstrings(self, s: str) -> int:
        # Dynamic Programming | Time: O(n) | Space: O(n),
        pass

