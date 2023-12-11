#ifndef _SOLUTION_H_
#define _SOLUTION_H_
#include <iostream>
#include <vector>

class Solution {
public:
    Solution(){};
    ~Solution(){};
    std::vector<int> twoSum(std::vector<int>& numbers, int target);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    std::vector<int> twoSum(std::vector<int>& numbers, int target);
};

#endif
