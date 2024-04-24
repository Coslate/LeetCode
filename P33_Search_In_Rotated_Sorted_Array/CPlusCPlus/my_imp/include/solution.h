#ifndef _SOLUTION_H_
#define _SOLUTION_H_
#include <iostream>
#include <vector>

class Solution {
public:
    Solution(){};
    ~Solution(){};
    int findMinPtr(std::vector<int>& nums);
    int binSearch(int left_ptr, int right_ptr, std::vector<int>& nums, const int target);
    int search(std::vector<int>& nums, int target);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    int search(std::vector<int>& nums, int target);
};

#endif
