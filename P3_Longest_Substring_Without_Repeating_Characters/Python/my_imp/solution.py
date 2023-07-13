
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Two Pointers + Sliding Window | Time: O(n) | Space: O(n)
        left_ptr  = 0
        hash_map  = {}
        longest_window_size = 0

        for right_ptr, each_char in enumerate(s):
            if each_char in hash_map:
                left_ptr = max(left_ptr, hash_map[each_char] + 1)

            hash_map[each_char] = right_ptr
            longest_window_size = max(longest_window_size, right_ptr-left_ptr+1)

        return longest_window_size




