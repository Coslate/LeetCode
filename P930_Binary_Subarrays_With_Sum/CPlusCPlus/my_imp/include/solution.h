#ifndef _SOLUTION_H_
#define _SOLUTION_H_
#include <iostream>  //std::cout
#include <vector>
#include <algorithm> //std::min
#include <unordered_map> //std::unordered_map

class Solution {
public:
    Solution(){};
    ~Solution(){};
    int numSubarraysWithSum(std::vector<int>& nums, int goal);
    int atMost(std::vector<int>& nums, int k);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    int numSubarraysWithSum(std::vector<int>& nums, int goal);
};

#endif
