#ifndef _SOLUTION_H_
#define _SOLUTION_H_
#include <vector>
#include <iostream>

class Solution {
public:
    Solution(){};
    ~Solution(){};
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n);
};

#endif
