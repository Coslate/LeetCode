#include <iostream>
#include <cstdlib>
#include <climits>
#include <vector>
#include <solution.h>
#include <cstring>
#include <string>

void printArray(const std::vector<int> &in, const std::string name);
std::ostream & operator << (std::ostream &out, const std::vector<int> &in);
std::ostream & operator << (std::ostream &out, const std::vector<std::vector<char>> &in);

int main(){
    Solution sol;
    OptSolution opt_sol;
    int ans;
    std::vector<std::vector<char>> board  = {
        {'5','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}
    };

    std::cout<<"//Case1:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"board = "<<board<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    //ans = sol.isValidSudoku(board);
    ans = opt_sol.isValidSudoku(board);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    board = {
        {'8','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}
    };

    std::cout<<"//Case2:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"board = "<<board<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    //ans = sol.isValidSudoku(board);
    ans = opt_sol.isValidSudoku(board);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;



    return EXIT_SUCCESS;
}

std::ostream & operator << (std::ostream &out, const std::vector<int> &in){
    std::cout<<"[";
    size_t in_size = in.size();

    if(in_size == 0){
        std::cout<<"]";
    }else{
        for (size_t i = 0; i < in_size; ++i){
            if(i == in.size()-1){
                std::cout<<in[i]<<"]";
            }else{
                std::cout<<in[i]<<", ";
            }
        }
    }
    return out;
}

std::ostream & operator << (std::ostream &out, const std::vector<std::vector<char>> &in){
    std::cout<<"["<<std::endl;

    if(in.size() == 0){
        std::cout<<"]";
        return out;
    }

    size_t row_num = in.size();
    size_t col_num = in[0].size();

    for(size_t i = 0; i < row_num; ++i){
        std::cout<<"[";
        for(size_t j = 0; j < col_num; ++j){
            if(j == col_num-1){
                std::cout<<in[i][j]<<"]"<<std::endl;
            }else{
                std::cout<<in[i][j]<<", ";
            }
        }
    }
    std::cout<<"]"<<std::endl;
    return out;
}

void printArray(const std::vector<int> &in, std::string name){
    std::cout<<name<<" = "<<"[";
    for (size_t i=0; i<in.size(); ++i){
        if(i == in.size()-1){
            std::cout<<in[i]<<"]"<<std::endl;
        }else{
            std::cout<<in[i]<<", ";
        }
    }

}
