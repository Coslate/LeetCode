#include <iostream>
#include <cstdlib>
#include <climits>
#include <vector>
#include <solution.h>
#include <cstring>
#include <string>

void printArray(const std::vector<char> &in, const std::string name);
std::ostream & operator << (std::ostream &out, const std::vector<char> &in);
std::ostream & operator << (std::ostream &out, const std::vector<std::vector<char>> &in);

int main(){
    Solution sol;
    OptSolution opt_sol;
    bool ans;
    std::vector<std::vector<char>> board  = {
        {'A', 'B', 'C', 'E'},
        {'S', 'F', 'C', 'S'},
        {'A', 'D', 'E', 'E'}
    };
    std::string word = "ABCCED";

    std::cout<<"//Case1:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"board = "<<board<<std::endl;
    std::cout<<"word = "<<word<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.exist(board, word);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    std::vector<std::vector<char>> board2  = {
        {'A','B','C','E'},
        {'S','F','C','S'},
        {'A','D','E','E'}
    };
    std::string word2 = "SEE";

    std::cout<<"//Case2:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"board2 = "<<board2<<std::endl;
    std::cout<<"word2 = "<<word2<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.exist(board2, word2);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    std::vector<std::vector<char>> board3  = {
        {'A','B','C','E'},
        {'S','F','C','S'},
        {'A','D','E','E'}
    };
    std::string word3 = "ABCB";

    std::cout<<"//Case3:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"board3 = "<<board3<<std::endl;
    std::cout<<"word3 = "<<word3<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.exist(board3, word3);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    std::vector<std::vector<char>> board4  = {
        {'A','B','C','E'},
        {'S','F','E','S'},
        {'A','D','E','E'}
    };
    std::string word4 = "ABCESEEEFS";

    std::cout<<"//Case4:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"board4 = "<<board4<<std::endl;
    std::cout<<"word4 = "<<word4<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.exist(board4, word4);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    return EXIT_SUCCESS;
}

std::ostream & operator << (std::ostream &out, const std::vector<char> &in){
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

void printArray(const std::vector<char> &in, std::string name){
    std::cout<<name<<" = "<<"[";
    for (size_t i=0; i<in.size(); ++i){
        if(i == in.size()-1){
            std::cout<<in[i]<<"]"<<std::endl;
        }else{
            std::cout<<in[i]<<", ";
        }
    }

}
