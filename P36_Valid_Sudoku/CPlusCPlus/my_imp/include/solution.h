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
    bool rowCheck(std::vector<std::vector<char>>& board, const int row_num, const int col_num);
    bool colCheck(std::vector<std::vector<char>>& board, const int row_num, const int col_num);
    bool boxCheck(std::vector<std::vector<char>>& board, const int row_num, const int col_num);
    bool isValidSudoku(std::vector<std::vector<char>>& board);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    bool getBit(const int x, const int val);
    bool isValidSudoku(std::vector<std::vector<char>>& board);
};

#endif
