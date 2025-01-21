from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import Counter, deque
import math
import numpy as np
import heapq
import random

class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:    
        # Time: O(m*n) | Space: O(m*n)
        # Dynamic Programming
        # Where m is the size of text, and n is the size of pattern.
        # https://leetcode.com/problems/regular-expression-matching/editorial/?envType=problem-list-v2&envId=plakya4j

        p_len = len(pattern)
        t_len = len(text)
        dp = [[False]*(p_len+1) for _ in range(t_len+1)] #(t_len+1)*(p_len+1)

        dp[-1][-1] = True # Empaty text matches empty pattern
        for i in range(t_len, -1, -1):
            for j in range(p_len-1, -1, -1): 
                #We don't need j==p_len, because empty pattern only matches empty text, which is d[-1][-1] = True, other cases under j==p_len is false.
                first_match = i < t_len and pattern[j] in {text[i], '.'}
                if j + 1 < p_len and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]




