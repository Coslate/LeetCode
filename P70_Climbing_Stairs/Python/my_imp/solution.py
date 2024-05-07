from typing import Optional, List
import math
from numpy.linalg import matrix_power
import numpy as np

class Solution:
    def climbStairs(self, n: int) -> int:
        # Dynamic Programming | Time: O(n) | Space: O(1), n is the input number
        # P(n) = P(n-1)+P(n-2), P(1) = 1, P(2) = 2, P(3) = 3, P(4) = 5
        if n == 1:
            return 1
        elif n == 2:
            return 2

        p = [0]*(n+1)
        p[1] = 1
        p[2] = 2

        for i in range(3, n+1):
            p[i] = p[i-1]+p[i-2]

        return p[n]

class OptSolution:
    def climbStairs(self, n: int) -> int:
        # Dynamic Programming | Binets Method | Time: O(logn) | Space: O(1), n is the input number
        # P(n) = P(n-1)+P(n-2), P(1) = 1, P(2) = 2, P(3) = 3, P(4) = 5
        q = np.array([[1, 1], [1, 0]])
        res = self.matrixPower(q, n)
        return res[0][0]

    def matrixPower(self, q: [[int]], n:int) -> [[int]]:
        ret = np.array([[1, 0], [0, 1]]) #I
        a = np.array([row[:] for row in q])

        while n != 0:
            if n & 1 == 1: #odd
                ret = ret @ a

            n = n >> 1
            a = a @ a

        return ret

    def climbStairsUsingMatrixPower(self, n: int) -> int:
        # Dynamic Programming | Binets Method | Time: O(logn) | Space: O(1), n is the input number
        # P(n) = P(n-1)+P(n-2), P(1) = 1, P(2) = 2, P(3) = 3, P(4) = 5
        q = [[1, 1], [1, 0]]
        res = matrix_power(q, n)
        return res[0][0]

    def climbStairsUsingDP(self, n: int) -> int:
        # Dynamic Programming | Time: O(n) | Space: O(1), n is the input number
        # P(n) = P(n-1)+P(n-2), P(1) = 1, P(2) = 2, P(3) = 3, P(4) = 5
        if n == 1:
            return 1
        elif n == 2:
            return 2

        p = [0]*(n+1)
        p[1] = 1
        p[2] = 2

        for i in range(3, n+1):
            p[i] = p[i-1]+p[i-2]

        return p[n]
