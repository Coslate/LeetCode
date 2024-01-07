#include <iostream>
#include <cstdlib>
#include <climits>
#include <vector>
#include <solution.h>
#include <cstring>
#include <string>

void printArray(const std::vector<int> &in, const std::string name);
std::ostream & operator << (std::ostream &out, const std::vector<int> &in);
std::ostream & operator << (std::ostream &out, const std::vector<std::vector<int>> &in);

int main(){
    Solution sol;
    OptSolution opt_sol;
    std::vector<std::vector<int>> matrix  = {
        {1, 1, 1},
        {1, 0, 1},
        {1, 1, 1},
    };

    std::cout<<"//Case1:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"matrix = "<<matrix<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    //sol.setZeroes(matrix);
    opt_sol.setZeroes(matrix);
    std::cout<<"matrix = "<<matrix<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    std::vector<std::vector<int>> matrix2  = {
        {0, 1, 2, 0},
        {3, 4, 5, 2},
        {1, 3, 1, 5},
    };

    std::cout<<"//Case2:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"matrix2 = "<<matrix2<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    //sol.setZeroes(matrix2);
    opt_sol.setZeroes(matrix2);
    std::cout<<"matrix2 = "<<matrix2<<std::endl;
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

std::ostream & operator << (std::ostream &out, const std::vector<std::vector<int>> &in){
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
