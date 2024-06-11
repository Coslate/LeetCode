#ifndef _SOLUTION_H_
#define _SOLUTION_H_
#include <iostream>
#include <vector>

class Solution {
public:
    Solution(){};
    ~Solution(){};
    int lengthOfLIS(std::vector<int>& nums);
    void printArray(const int* const &in, std::string name, const int in_size);
    void printArray(const std::vector<int> &in, std::string name);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    int binarySearch(const std::vector<int>& nums, const int target);
    int lengthOfLIS(std::vector<int>& nums);
};

#endif
