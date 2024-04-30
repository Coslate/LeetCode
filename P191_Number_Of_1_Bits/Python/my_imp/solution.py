from typing import Optional, List
import math

class Solution:
    def hammingWeight(self, n: int) -> int:
        # Bit Operation | Time: O(logn) | Space: O(1), n is the input number
        result = 0

        while n > 0:
            mod = n%2
            n //= 2

            if mod == 1:
                result += 1

            if n == 2:
                result += 1
                break

        return result

class OptSolution:
    def hammingWeight(self, n: int) -> int:
        # Bit Operation | Time: O(1) | Space: O(1), n is the input number
        result = 0
        mask   = 1
        for i in range(32):
            if (n & mask) != 0:
                result += 1
            mask = mask << 1

        return result

