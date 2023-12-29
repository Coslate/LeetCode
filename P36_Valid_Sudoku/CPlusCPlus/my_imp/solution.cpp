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
    //Matrix | Time: O(n^2) | Space: O(n^2), n is the height or width of the board
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

bool OptSolution::getBit(const int x, const int val){
    return (x>>val) & 1;
}
bool OptSolution::isValidSudoku(std::vector<std::vector<char>>& board){
    //Bitmasking | Time: O(n^2) | Space: O(n), n is the height or width of the board
    int row_num = (int)board.size();
    int col_num = (int)board[0].size();
    std::vector<int> row_check_bitarr(row_num);
    std::vector<int> col_check_bitarr(col_num);
    std::vector<int> box_check_bitarr(int((row_num/3)*(col_num/3)));

    for(int i = 0; i < row_num; ++i){
        for(int j = 0; j < col_num; ++j){
            if(board[i][j] == '.'){
                continue;
            }else{
                int val = (int)board[i][j] - int('0');
                int box_pos = (i/3)*3 + (j/3);
                if(getBit(row_check_bitarr[i], val) || getBit(col_check_bitarr[j], val) || getBit(box_check_bitarr[box_pos], val)){
                    return false;
                }

                int val_bit = (1<<val);
                row_check_bitarr[i] |= val_bit;
                col_check_bitarr[j] |= val_bit;
                box_check_bitarr[box_pos] |= val_bit;
            }
        }
    }
    return true;
}

