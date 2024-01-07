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
    void setBits(int (&bit_reg)[1250], const int num);
    int getBits(const int (&bit_reg)[1250], const int num);
    void setRowZeroes(const int index_i, const int col_num, std::vector<std::vector<int>>& matrix);
    void setColZeroes(const int index_j, const int row_num, std::vector<std::vector<int>>& matrix);
    void setZeroes(std::vector<std::vector<int>>& matrix);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    void setZeroes(std::vector<std::vector<int>>& matrix);
};

#endif
