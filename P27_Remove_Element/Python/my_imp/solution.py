from typing import Optional, List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Time: O(n) | Space: O(n)
        result_list = []

        for index, elem in enumerate(nums):
            if elem != val:
                result_list.append(elem)

        nums[:] = result_list[:]
        return len(result_list)




class OptSolution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Time: O(n) | Space: O(1)
        mod_index = 0

        for index, elem in enumerate(nums):
            if elem != val:
                nums[mod_index] = nums[index]
                mod_index += 1

        return mod_index

