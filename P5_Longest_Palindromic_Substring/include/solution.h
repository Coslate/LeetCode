#ifndef _SOLUTION_H_
#define _SOLUTION_H_
#include <cstring>

class Solution {
public:
    Solution(){};
    ~Solution(){};

    void swap(char& ch_a, char& ch_b);
    void reverseStrRef(std::string& s);
    std::string reverseStrCpy(const std::string &s);
    std::string longestPalindrome(std::string s);
};

#endif
