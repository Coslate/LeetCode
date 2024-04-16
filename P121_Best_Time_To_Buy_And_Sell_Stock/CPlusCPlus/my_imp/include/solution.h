#ifndef _SOLUTION_H_
#define _SOLUTION_H_
#include <iostream>
#include <vector>

class Solution {
public:
    Solution(){};
    ~Solution(){};
    int maxProfit(std::vector<int>& prices);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    int maxProfit(std::vector<int>& prices);
};

#endif
