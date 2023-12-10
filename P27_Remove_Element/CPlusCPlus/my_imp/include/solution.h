#ifndef _SOLUTION_H_
#define _SOLUTION_H_
#include <vector>
#include <iostream>

class Solution {
public:
    Solution(){};
    ~Solution(){};
    int removeElement(std::vector<int>& nums, int val);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    int removeElement(std::vector<int>& nums, int val);
};

#endif
