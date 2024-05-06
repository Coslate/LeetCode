from typing import Optional, List
import math

class Solution:
    def reverseBits(self, n: int) -> int:
        # Bit Operation | Time: O(1) | Space: O(1), n is the input number
        result = 0
        power = 31

        while n != 0:
            least_bit = n & 1
            result += (least_bit << power)
            n = n >> 1
            power -= 1

        return result


class OptSolution:
    #@functools.lru_cache(maxsize=256)
    def reverseNbits(self, n: int, k: int) -> int:
        result = 0
        power = k-1

        while n!= 0:
            result += (n&1) << power
            n = n >> 1
            power -= 1
        return result

    def reverseBits(self, n: int) -> int:
        # Bit Operation | Cache Memorization + MultipleBits Processing |Time: O(1) | Space: O(1), n is the input number
        result = 0
        k_bits = 8
        power = 31 - (k_bits-1)
        cache = {}
        mask = 0
        shift_bit = 0

        while shift_bit < k_bits:
            mask += 1 << shift_bit
            shift_bit += 1

        while n != 0:
            least_bytes = n &mask
            if(least_bytes in cache):
                reversed_bytes = cache[least_bytes]
            else:
                reversed_bytes = self.reverseNbits(least_bytes, k_bits)
                cache[least_bytes] = reversed_bytes
            result += reversed_bytes << power
            n = n >> k_bits
            power -= k_bits

        return result
