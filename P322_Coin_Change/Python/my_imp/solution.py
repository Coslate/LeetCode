from typing import Optional, List
import math
from numpy.linalg import matrix_power
import numpy as np

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dynamic Programming | Time: O(n) | Space: O(1), n is the input number
        dp = [float('inf')]*(amount+1)

        for coin in coins:


class OptSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dynamic Programming | Time: O(logn) | Space: O(1), n is the input number
        pass
