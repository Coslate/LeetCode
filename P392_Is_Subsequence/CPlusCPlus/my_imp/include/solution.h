#ifndef _SOLUTION_H_
#define _SOLUTION_H_
#include <iostream>
#include <string>

class Solution {
public:
    Solution(){};
    ~Solution(){};
    bool isSubsequence(std::string s, std::string t);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    bool isSubsequence(std::string s, std::string t);
};

#endif
