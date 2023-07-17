from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> str:
        # Two Pointers | Time: O(n) | Space: O(1)
        left = 0
        right = len(height)-1
        area_max = -1

        while left < right:
            area_max = max(area_max, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area_max
