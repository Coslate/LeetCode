#ifndef _SOLUTION_H_
#define _SOLUTION_H_
#include <iostream>  //std::cout
#include <vector>
#include <algorithm> //std::min

class Solution {
public:
    Solution(){};
    ~Solution(){};
    int minSubArrayLen(int target, std::vector<int>& nums);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    int minSubArrayLen(int target, std::vector<int>& nums);
};

#endif
