from typing import Optional, List
import math

class Solution:
    def hammingWeight(self, n: int) -> int:
        # Bit Operation | Time: O(1) | Space: O(1), n is the input number
        result = 0
        mask   = 1
        for i in range(32):
            if (n & mask) != 0:
                result += 1
            mask = mask << 1

        return result

    def countBits(self, n: int) -> List[int]:
        # Bit Operation | Time: O(n) | Space: O(1), n is the input length of
        # array
        result = []
        for i in range(n+1):
            result.append(self.hammingWeight(i))

        return result

class OptSolution:
    def countBits(self, n: int) -> List[int]:
        # Bit Operation | Dynamic Programming | Time: O(n) | Space: O(1), n is the input length of
        # array
        result = [0]*(n+1)

        for i in range(1, n+1):
            #P(x) = P(x/2) + (x mod 2)
            #e.g. count_of_1(1001011101) = count_of_1(100101110) + (1001011101) mod 2
            result[i] = result[i>>1] + (i & 1)

        return result
