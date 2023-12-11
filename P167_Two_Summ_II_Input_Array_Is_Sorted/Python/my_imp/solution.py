from typing import Optional, List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two Pointers | Time: O(n) | Space: O(1)
        ptr_l = 0
        ptr_r = len(numbers)-1
        result = []
        while ptr_l < ptr_r:
            if numbers[ptr_l] + numbers[ptr_r] > target:
                ptr_r -= 1
            elif numbers[ptr_l] + numbers[ptr_r] < target:
                ptr_l += 1
            else:
                result.append(ptr_l+1)
                result.append(ptr_r+1)
                break

        return result

class OptSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two Pointers | Time: O(n) | Space: O(1), n is the size of t
        # Same as the twoSum() in Solution class (above).
        pass


