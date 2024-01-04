#include <solution.h>

void Solution::setBits(int (&bit_reg)[1250], const int num){
    int index_group = num/32;
    int bit = num%32;
    bit_reg[index_group] |= 1 << bit;
}

int Solution::getBits(const int (&bit_reg)[1250], const int num){
    int index_group = num/32;
    int bit = num%32;
    return bit_reg[index_group] >> bit & 1;
}

void Solution::setRowZeroes(const int index_i, const int col_num, std::vector<std::vector<int>>& matrix){
    for(int j = 0; j < col_num; ++j){
        matrix[index_i][j] = 0;
    }
}

void Solution::setColZeroes(const int index_j, const int row_num, std::vector<std::vector<int>>& matrix){
    for(int i = 0; i < row_num; ++i){
        matrix[i][index_j] = 0;
    }
}

void Solution::setZeroes(std::vector<std::vector<int>>& matrix){
    //Matrix | Time: O(n^2) | Space: O(1), n is the height or width of the matrix
    int bit_reg[1250] = {0};//40000/32 = 1250
    int row_num = (int)matrix.size();
    int col_num = (int)matrix[0].size();

    for(int i=0; i<row_num; ++i){
        for(int j=0; j<col_num; ++j){
            if(matrix[i][j] == 0){
                int num = i*col_num + j;
                setBits(bit_reg, num);
            }
        }
    }

    for(int i=0; i<row_num; ++i){
        for(int j=0; j<col_num; ++j){
            int num = i*col_num + j;
            if(getBits(bit_reg, num) == 1){
                setRowZeroes(i, col_num, matrix);
                setColZeroes(j, row_num, matrix);
            }
        }
    }
}

void OptSolution::setZeroes(std::vector<std::vector<int>>& matrix){
    //Bitmasking | Time: O(n^2) | Space: O(n), n is the height or width of the matrix
    //
    matrix[0][0] = 10000;
}

