from typing import Optional, List
import math
from numpy.linalg import matrix_power
import numpy as np

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dynamic Programming | Time: O(S*n) | Space: O(n), n is the length of coins, S is the amount.
        if amount == 0:
            return 0

        dp = [float('inf')]*(amount+1)

        for i in range(amount+1):
            for coin in coins:
                if i-coin < 0:
                    continue
                elif i == coin: # i-coin == 0
                    dp[i] = 1
                else: # i-coin > 0
                    dp[i] = min(dp[i-coin]+1, dp[i])
        return dp[amount] if dp[amount] != float('inf') else -1

class OptSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dynamic Programming | Time: O(S*n) | Space: O(n), n is the length of coins, S is the amount.
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i-coin]+1, dp[i])

        return dp[amount] if dp[amount] != float('inf') else -1

