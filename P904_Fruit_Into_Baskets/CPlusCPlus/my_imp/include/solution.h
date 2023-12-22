#ifndef _SOLUTION_H_
#define _SOLUTION_H_
#include <iostream>  //std::cout
#include <vector>
#include <stdlib.h> //abs
#include <algorithm> //std::min

class Solution {
public:
    Solution(){};
    ~Solution(){};
    int totalFruit(std::vector<int>& fruits);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    int totalFruit(std::vector<int>& fruits);
};

#endif
