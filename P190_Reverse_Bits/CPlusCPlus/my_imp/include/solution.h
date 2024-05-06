#ifndef _SOLUTION_H_
#define _SOLUTION_H_
#include <iostream>
#include <vector>

class Solution {
public:
    Solution(){};
    ~Solution(){};
    uint32_t reverseBits(uint32_t n);
    uint32_t reverseNBits(uint32_t n, uint32_t k);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    uint32_t reverseBits(uint32_t n);
};

#endif
