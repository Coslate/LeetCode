#include <solution.h>

bool Solution::rowCheck(std::vector<std::vector<char>>& board, const int row_num, const int col_num){
    for(int i = 0; i < row_num; ++i){
        std::unordered_map<int, int> mem_dict;

        for(int j = 0; j < col_num; ++j){
            if(board[i][j] == '.'){
                continue;
            }else{
                if(mem_dict.find(board[i][j]) != mem_dict.end()){
                    return false;
                }else{
                    mem_dict[board[i][j]] = 1;
                }
            }
        }
    }

    return true;
}
bool Solution::colCheck(std::vector<std::vector<char>>& board, const int row_num, const int col_num){
    for(int j = 0; j < col_num; ++j){
        std::unordered_map<int, int> mem_dict;

        for(int i = 0; i < row_num; ++i){
            if(board[i][j] == '.'){
                continue;
            }else{
                if(mem_dict.find(board[i][j]) != mem_dict.end()){
                    return false;
                }else{
                    mem_dict[board[i][j]] = 1;
                }
            }
        }
    }
    return true;
}
bool Solution::boxCheck(std::vector<std::vector<char>>& board, const int row_num, const int col_num){
    for(int i = 0; i < 3; ++i){
        for(int j = 0; j < 3; ++j){
            std::unordered_map<int, int> mem_dict;
            int grid_i = i*3;
            int grid_j = j*3;
            for(int k = 0; k < 3; ++k){
                for(int r = 0; r < 3; ++r){
                    int index_i = grid_i + k;
                    int index_j = grid_j + r;

                    if(board[index_i][index_j] == '.'){
                        continue;
                    }else{
                        if(mem_dict.find(board[index_i][index_j]) != mem_dict.end()){
                            return false;
                        }else{
                            mem_dict[board[index_i][index_j]] = 1;
                        }
                    }
                }
            }
        }
    }

    return true;
}
bool Solution::isValidSudoku(std::vector<std::vector<char>>& board){
    //Matrix | Time: O(n) | Space: O(n), n is the size of board
    int row_num = (int)board.size();
    int col_num = (int)board[0].size();

    if(!rowCheck(board, row_num, col_num)){
        return false;
    }
    if(!colCheck(board, row_num, col_num)){
        return false;
    }
    if(!boxCheck(board, row_num, col_num)){
        return false;
    }

    return true;
}

bool OptSolution::isValidSudoku(std::vector<std::vector<char>>& board){
    //Matrix | Time: O(n) | Space: O(n), n is the size of board
    Solution sol;
    return sol.isValidSudoku(board);
}

