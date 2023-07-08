from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash Table Implementation | Time: O(n) | Space: O(n)
        if not nums:
            return None

        in_mem = {}

        for index, x in enumerate(nums):
            if nums[index] in in_mem:
                return [in_mem[nums[index]], index]

            in_mem[target-nums[index]] = index


