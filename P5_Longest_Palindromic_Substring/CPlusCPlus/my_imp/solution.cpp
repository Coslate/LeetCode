#include <map>
#include <vector>
#include <cstdio>
#include <solution.h>
#include <cstring>
#include <string>
#include <iostream>

#define MAX_IN_STRLEN 1000

std::string Solution::longestPalindrome(std::string s){
    // Dynamic Programming | Time: Best: O(n), Worst: O(n^2) | Space: O(1)
    auto getLength = [&](const std::string &s, int l, int r){
        int n = s.length();
        while((l>=0) && (r < n) && (s[l] == s[r])){
            --l;
            ++r;
        }

        return r - l - 1;
    };

    int len_opt = -1;
    int start = 0;

    //search for the center
    for (size_t i=0; i<s.length();++i){
        int cur_len = std::max(getLength(s, (int)i, (int)i), getLength(s, (int)i, (int)(i+1)));
        if(cur_len > len_opt){
            len_opt = cur_len;
            start = i - (cur_len-1)/2;
        }
    }

    return s.substr(start, len_opt);
}
