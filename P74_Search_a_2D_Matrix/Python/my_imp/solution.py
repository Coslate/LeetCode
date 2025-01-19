from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import Counter, deque
import math
import numpy as np
import heapq
import random

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:    
        # Time: O(log(m*n)) | Space: O(1)
        # Where m, n are the rows and cols of matrix
        # https://leetcode.com/problems/search-a-2d-matrix/editorial/?envType=problem-list-v2&envId=plakya4j

        m = len(matrix)

        if m == 0:
            return False
        
        n = len(matrix[0])

        left = 0
        right = m*n

        while left < right:
            mid = (left + right)//2
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid

        return False







