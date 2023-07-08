from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash Table Implementation | Time: O(n) | Space: O(n)
        hash_map = {}

        for index, x in enumerate(nums):
            complement = target-x

            if complement in hash_map:
                return [hash_map[complement], index]
            else:
                hash_map[x] = index
