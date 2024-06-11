#ifndef _SOLUTION_H_
#define _SOLUTION_H_
#include <iostream>
#include <vector>

class Solution {
public:
    Solution(){};
    ~Solution(){};
    int coinChange(std::vector<int>& coins, int amount);
    void printArray(const int* const &in, std::string name, const int in_size);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    int coinChange(std::vector<int>& coins, int amount);
};

#endif
