from typing import Optional, List
import collections

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Sliding Window | Time: O(n) | Space: O(1)
        basket0 = -1
        basket1 = -1
        b1_ptr  = 0
        b0_ptr  = 0
        ans = 0
        cur_size = 0
        fruit_size = len(fruits)

        for j in range(fruit_size):
            if basket0 == -1 and basket1 == -1:
                basket0 = fruits[j]
                cur_size += 1
                b0_ptr = j
            elif basket0 == -1 and fruits[j] != basket1:
                basket0 = fruits[j]
                cur_size += 1
                b0_ptr = j
            elif basket1 == -1 and fruits[j] != basket0:
                basket1 = fruits[j]
                cur_size += 1
                b1_ptr = j
            else:
                if fruits[j] == basket0:
                    cur_size += 1
                    if fruits[j-1] != fruits[j]:
                        b0_ptr = j
                elif fruits[j] == basket1:
                    cur_size += 1
                    if fruits[j-1] != fruits[j]:
                        b1_ptr = j
                else:
                    if basket0 == fruits[j-1]:
                        basket1 = fruits[j]
                        b1_ptr = j
                    else:
                        basket0 = fruits[j]
                        b0_ptr = j
                    ans = max(ans, cur_size)
                    cur_size = abs(b0_ptr-b1_ptr)+1

        ans = max(ans, cur_size)
        return ans

class OptSolution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Sliding Window | Time: O(n) | Space: O(1)
        # Same as above
        pass


