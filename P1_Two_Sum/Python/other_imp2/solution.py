from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Two Pointers Implementation | Time: O(nlogn) | Space: O(n)
        if not nums:
            return None

        #sorting
        result = []
        for i, num in enumerate(nums):
            result.append((num, i))

        result.sort(key=lambda x:x[0])

        #two pointers
        i, j = 0, len(result)-1
        while i<j: #overlap of i and j is not allowed since our mission is to find a 'pair'
            if result[i][0] + result[j][0] == target:
                return [result[i][1], result[j][1]] #correct pair found
            elif result[i][0] + result[j][0] < target:# too small, ++i
                i += 1
            else: #too large j--
                j -= 1

        return None
