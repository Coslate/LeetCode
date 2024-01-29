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
    std::vector<int> spiralOrder(std::vector<std::vector<int>>& matrix);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    std::vector<int> spiralOrder(std::vector<std::vector<int>>& matrix);
};

#endif
