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
    bool DFS(std::vector<std::vector<char>>& board, std::string word, int d, const int i, const int j, const int row_num, const int col_num);
    bool exist(std::vector<std::vector<char>>& board, std::string word);
};

class OptSolution {
public:
    OptSolution(){};
    ~OptSolution(){};
    bool exist(std::vector<std::vector<char>>& board, std::string word);
};

#endif
