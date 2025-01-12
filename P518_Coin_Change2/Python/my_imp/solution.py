from typing import Optional, List, Tuple, Dict, Deque, Set, Self, TypeVar
from collections import Counter
import math
import numpy as np
import heapq

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Time: O(N*amount) | Space: O(N*amount)
        # Where N is the number of elements in coins.
        # https://leetcode.com/problems/coin-change-ii/editorial/?envType=problem-list-v2&envId=plakya4j

        # dp[i][j]: ways to make up j amounts beginning from coin[i]
        # dp[i][0] is initialized to 1 as only one way to make up 0 amount: no selecting any coins
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        for i in range(n):
            dp[i][0] = 1

        for i in range(n-1, -1, -1):
            for j in range(1, amount+1):
                if coins[i] > j:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j-coins[i]]

        return dp[0][amount]

    def change_opt(self, amount: int, coins: List[int]) -> int:
        # Time: O(N*amount) | Space: O(amount)
        # Where N is the number of elements in coins.
        # https://leetcode.com/problems/coin-change-ii/editorial/?envType=problem-list-v2&envId=plakya4j

        # dp[j]: ways to make up j amounts
        # dp[0] is initialized to 1 as only one way to make up 0 amount: no selecting any coins
        n = len(coins)
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1

        for i in range(n-1, -1, -1):
            for j in range(coins[i], amount+1):
                dp[j] = dp[j] + dp[j-coins[i]]

        return dp[amount]

        