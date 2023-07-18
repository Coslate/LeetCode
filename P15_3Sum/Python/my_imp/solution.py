from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Two Pointers | Time: O(nlogn+n^2) | Space: O(1) (Do not consider
        # answer storing and output)
        ans = []
        nums_sorted = sorted(nums) #To remove the repeated triplet.

        for i, element in enumerate(nums_sorted):
            j = i+1
            k = len(nums)-1

            if i and nums_sorted[i]==nums_sorted[i-1]: continue #To remove the repeated triplet.

            while j < k:
                if nums_sorted[i] + nums_sorted[j] + nums_sorted[k] > 0:
                    k -= 1
                elif nums_sorted[i] + nums_sorted[j] + nums_sorted[k] < 0:
                    j += 1
                else:
                    ans.append([nums_sorted[i], nums_sorted[j], nums_sorted[k]])
                    while j < k and nums_sorted[j+1] == nums_sorted[j]:#To remove the repeated triplet.
                        j += 1
                    while k > j and nums_sorted[k-1] == nums_sorted[k]:#To remove the repeated triplet.
                        k -= 1

                    j += 1
                    k -= 1

        return ans
