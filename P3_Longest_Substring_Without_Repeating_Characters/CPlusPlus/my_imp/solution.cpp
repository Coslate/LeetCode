#include <map>
#include <vector>
#include <cstdio>
#include <solution.h>
#include <cstring>
#include <string>

#define MAX_CHARS_NUM 128

int Solution::lengthOfLongestSubstring(std::string s){
    // Two Pointers + Sliding Window | Time: O(n) | Space: O(n)
    int left_ptr  = 0;
    std::vector<int> hash_map(128, -1);//keep the latest position of occured char.
    int longest_window_size = 0;

    for (size_t right_ptr = 0; right_ptr < s.length(); ++right_ptr){
        left_ptr = std::max(left_ptr, hash_map[(int)s[right_ptr]]+1);
        hash_map[(int)s[right_ptr]] = (int)right_ptr;
        longest_window_size = std::max(longest_window_size, (int)right_ptr-left_ptr+1);
    }

    return longest_window_size;
}
