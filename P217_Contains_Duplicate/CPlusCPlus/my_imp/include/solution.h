#ifndef _SOLUTION_H_
#define _SOLUTION_H_
#include <iostream>
#include <vector>

class Solution {
public:
    Solution(){};
    ~Solution(){};
    bool containsDuplicate(std::vector<int>& nums);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    bool containsDuplicate(std::vector<int>& nums);
};

#endif
