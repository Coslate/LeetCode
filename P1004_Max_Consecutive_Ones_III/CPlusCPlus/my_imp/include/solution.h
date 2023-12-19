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
    int longestOnes(std::vector<int>& nums, int k);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    int longestOnes(std::vector<int>& nums, int k);
};

#endif
