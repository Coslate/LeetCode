from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import Counter, deque
import math
import numpy as np
import heapq
import random

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:    
        # Time: O(4^n/sqrt(n)) | Space: O(4^n/sqrt(n))
        # Divide and Conquer
        # The number of branch is T(n) = sum_k_0_to_n-1(T(k)T(n-1-k)) = C(n), where C(n) is the Catalan Number
        # For each branch we need to append(left+"("+right_str+")"), taking O(n) to construct the string.
        # So the total Time Complexity is O(n)*O(C(n)) = O(n)*O(4^n/(n*sqrt(n))) = O(4^n/sqrt(n))
        # Space Complexity is the same, except that the O(n) comes from the number of call in each branch:
        # In each branch of T(k) and T(n-1-k), we need total of O(n) recursive call, so the total space
        # complexity is O(n)*O(C(n)) = O(4^n/sqrt(n))
        # Where n is the pair number of parentheses.
        # https://leetcode.com/problems/generate-parentheses/editorial/?envType=problem-list-v2&envId=plakya4j

        if n == 0:
            return [""]

        ans = []
        for left_count in range(n):
            for left_str in self.generateParenthesis(left_count):
                for right_str in self.generateParenthesis(n-1-left_count):
                    ans.append(left_str+"("+right_str+")")

        return ans