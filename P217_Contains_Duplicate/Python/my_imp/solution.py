from typing import Optional, List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Array | Time: O(n) | Space: O(1), n is the size of prices[]
        num_dict = {}

        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                return True
        return False

class OptSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Array | Time: O(n) | Space: O(1), n is the size of prices[]
        pass

