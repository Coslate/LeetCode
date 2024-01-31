#include <solution.h>

void Solution::rotate(std::vector<std::vector<int>>& matrix){
    //Matrix | Time: O(n^2) | Space: O(1), n is the height or width of the matrix
    int row_num = matrix.size();
    int col_num = row_num;

    //Transpose
    for(int i=0; i<row_num; ++i){
        for(int j=i+1; j<col_num; ++j){
            int tmp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = tmp;
        }
    }

    //Reverse
    for(int i=0; i<row_num; ++i){
        for(int j=0; j<col_num/2; ++j){
            int tmp = matrix[i][j];
            matrix[i][j] = matrix[i][col_num-j-1];
            matrix[i][col_num-j-1] = tmp;
        }
    }
}

void OptSolution::rotate(std::vector<std::vector<int>>& matrix){
    //Matrix | Time: O(n^2) | Space: O(1), n is the height or width of the matrix
    Solution sol;
    sol.rotate(matrix);
}

