from typing import Optional, List
import math

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Bit Operation | Time: O(1) | Space: O(1), n is the size of input array
        x = abs(a)
        y = abs(b)

        if x < y:
            return self.getSum(b, a)

        sign = 1 if a >= 0 else -1

        if a*b >= 0:
            # x+y
            while y != 0:
                add_wo_carry = x^y
                carry        = (x&y)<<1

                x = add_wo_carry
                y = carry
        else:
            # x-y
            while y != 0:
                sub_wo_borrow = x^y
                borrow        = ((~x)&y)<<1

                x = sub_wo_borrow
                y = borrow

        return sign*x

class OptSolution:
    def getSum(self, a: int, b: int) -> int:
        # Bit Operation | Time: O(1) | Space: O(1), n is the size of input array
        pass

