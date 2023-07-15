
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Dynamic Programming | Time: Best: O(n), Worst: O(n^2) | Space: O(1)
        def get_length(s: str, l: int, r: int) -> int:
            n = len(s)
            while l>=0 and r < n and s[l]==s[r]:
                l -= 1
                r += 1

            return r - l - 1

        len_opt = -1
        start = 0

        #search for the center
        for index, char_x in enumerate(s):
            cur_len = max(get_length(s, index, index), get_length(s, index, index+1))
            if cur_len > len_opt:
                len_opt = cur_len
                start = index - (len_opt-1)//2

        return s[start:start+len_opt]
