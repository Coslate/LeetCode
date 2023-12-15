#ifndef _SOLUTION_H_
#define _SOLUTION_H_
#include <iostream>  //std::cout
#include <vector>
#include <algorithm> //std::min

class Solution {
public:
    Solution(){};
    ~Solution(){};
    int numberOfSubarrays(std::vector<int>& nums, int k);
    int atMost(std::vector<int> &nums, int k);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    int numberOfSubarrays(std::vector<int>& nums, int k);
};

#endif
