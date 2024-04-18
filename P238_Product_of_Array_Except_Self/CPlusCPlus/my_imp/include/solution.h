#ifndef _SOLUTION_H_
#define _SOLUTION_H_
#include <iostream>
#include <vector>

class Solution {
public:
    Solution(){};
    ~Solution(){};
    std::vector<int> productExceptSelf(std::vector<int>& nums);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    std::vector<int> productExceptSelf(std::vector<int>& nums);
};

#endif
