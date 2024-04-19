#ifndef _SOLUTION_H_
#define _SOLUTION_H_
#include <iostream>
#include <vector>

class Solution {
public:
    Solution(){};
    ~Solution(){};
    int maxSubArrayRangeSearch(const int left_idx, const int right_idx, const std::vector<int> &nums);
    int maxSubArray(std::vector<int>& nums);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    int maxSubArray(std::vector<int>& nums);
};

#endif
