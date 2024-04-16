from typing import Optional, List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Array | Time: O(n) | Space: O(1), n is the size of prices[]
        max_prof = 0
        record_min = prices[0]

        for ptr in range(len(prices)):
            if prices[ptr] > record_min:
                max_prof = max(max_prof, prices[ptr] - record_min)
            else:
                record_min = prices[ptr]

        return max_prof

class OptSolution:
    def maxProfit(self, prices: List[int]) -> int:
        # Array | Time: O(n) | Space: O(1), n is the size of prices[]

