from typing import Optional, List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time: O(n) | Space: O(n)
        alnum_list_inv = []
        alnum_list = [x.lower() for x in s if x.isalnum()]
        alnum_list_inv[:] = alnum_list[::-1]
        ans = False

        if(alnum_list == alnum_list_inv):
            ans = True

        return ans

class OptSolution:
    def isPalindrome(self, s: str) -> bool:
        # Time: O(n) | Space: O(1)
        s_length = len(s)
        if s_length == 0:
            return True

        ptr_l = 0
        ptr_r = s_length-1
        ans = True

        while ptr_l <= ptr_r:
            if not s[ptr_l].isalnum():
                ptr_l += 1
            elif not s[ptr_r].isalnum():
                ptr_r -= 1
            else:
                if s[ptr_l].lower() != s[ptr_r].lower():
                    ans = False
                    break
                else:
                    ptr_l += 1
                    ptr_r -= 1

        return ans
