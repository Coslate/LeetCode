from typing import Optional, List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Array | Time: O(n) | Space: O(n), n is the size of input array
        answer = []
        left_prod_list = []
        right_prod_list = []
        left_prod = 1
        right_prod = 1

        for i in range(len(nums)):
            if i != 0:
                left_prod *= nums[i-1]
            left_prod_list.append(left_prod)

        for i in range(len(nums)-1, -1, -1):
            if i != len(nums)-1:
                right_prod *= nums[i+1]
            right_prod_list.insert(0, right_prod)

        for i in range(len(nums)):
            answer.append(left_prod_list[i]*right_prod_list[i])

        return answer

class OptSolution:
    def productExceptSelf(self, nums: List[int]) -> bool:
        # Array | Time: O(n) | Space: O(1), n is the size of input array
        answer = []
        left_prod = 1
        right_prod = 1

        for i in range(len(nums)):
            if i != 0:
                left_prod *= nums[i-1]
            answer.append(left_prod)

        for i in range(len(nums)-1, -1, -1):
            if i != len(nums)-1:
                right_prod *= nums[i+1]
            answer[i] *= right_prod

        return answer

