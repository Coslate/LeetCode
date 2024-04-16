#include <solution.h>

bool Solution::DFS(std::vector<std::vector<char>>& board, std::string word, int d, const int i, const int j, const int row_num, const int col_num){
    if(i < 0 or i > row_num-1 or j < 0 or j > col_num-1){
        return false;
    }else if(board[i][j] != word[d]){
        return false;
    }else if(d == int(word.length())-1){
        return true;
    }else{
        char org = board[i][j];
        board[i][j] = 0;
        bool result = DFS(board, word, d+1, i, j+1, row_num, col_num) |
                      DFS(board, word, d+1, i, j-1, row_num, col_num) |
                      DFS(board, word, d+1, i+1, j, row_num, col_num) |
                      DFS(board, word, d+1, i-1, j, row_num, col_num);
        board[i][j] = org;

        return result;
    }
}

bool Solution::exist(std::vector<std::vector<char>>& board, std::string word){
    //Matrix | Time: O(m*n*4^l) | Space: O(m*n + l)
    int row_num = board.size();
    int col_num = board[0].size();

    for(int i=0; i<row_num; ++i){
        for(int j=0; j<col_num; ++j){
            if(DFS(board, word, 0, i, j, row_num, col_num)){
                return true;
            }
        }
    }
    return false;
}

bool OptSolution::exist(std::vector<std::vector<char>>& board, std::string word){
    //Matrix | Time: O(m*n*4^l) | Space: O(m*n + l)
    Solution sol;
    return sol.exist(board, word);
}

