from typing import Optional, List
import collections

class Solution:
    def balancedString(self, s: str) -> int:
        # Sliding Window | Time: O(n) | Space: O(1)
        count = collections.Counter(s)
        s_size = len(s)
        ans_num = s_size
        avg_thr = s_size//4
        i = 0

        for j in range(s_size):
            count[s[j]] -= 1
            while i < s_size and all([count['Q'] <= avg_thr, count['R'] <= avg_thr, count['W'] <= avg_thr, count['E'] <= avg_thr]):
                ans_num = min(ans_num, j-i+1)
                count[s[i]] += 1
                i += 1

        return ans_num

class OptSolution:
    def balancedString(self, s: str) -> int:
        # Sliding Window | Time: O(n) | Space: O(1)
        # Same as above
        pass


