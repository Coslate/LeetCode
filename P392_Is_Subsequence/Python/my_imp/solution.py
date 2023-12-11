from typing import Optional, List

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Time: O(n) | Space: O(1), m is the size of s, n is the size of t
        start_index = 0
        end_index = len(t)
        ans = True

        for ele_s in s:
            ele_s_exist = False

            for index in range(start_index, end_index):
                if t[index] == ele_s:
                    ele_s_exist = True
                    start_index = index+1
                    break

            if not ele_s_exist:
                ans = False
                break

        return ans

class OptSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Two Pointers | Time: O(n) | Space: O(1), n is the size of t
        n = len(t)
        m = len(s)
        index_j = 0
        ans     = False

        if m > n:
            return False

        if m == 0:
            return True

        for index_i, ele in enumerate(t):
            if s[index_j] == ele:
                index_j += 1
                if index_j == m:
                    ans = True
                    break

        return ans


