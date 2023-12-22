#include <iostream>
#include <cstdlib>
#include <climits>
#include <vector>
#include <solution.h>
#include <cstring>
#include <string>

void printArray(const std::vector<int> &in, const std::string name);
std::ostream & operator << (std::ostream &out, const std::vector<int> &in);

int main(){
    Solution sol;
    OptSolution opt_sol;
    int ans;
    std::vector<int> fruits = {1, 2, 1};

    std::cout<<"//Case1:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"fruits = "<<fruits<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.totalFruit(fruits);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    fruits = {0, 1, 2, 2};
    std::cout<<"//Case2:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"fruits = "<<fruits<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.totalFruit(fruits);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    fruits = {1, 2, 3, 2, 2};
    std::cout<<"//Case3:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"fruits = "<<fruits<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.totalFruit(fruits);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    fruits = {3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4};
    std::cout<<"//Case4:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"fruits = "<<fruits<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.totalFruit(fruits);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    fruits = {0, 1, 6, 6, 4, 4, 6};
    std::cout<<"//Case5:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"fruits = "<<fruits<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.totalFruit(fruits);
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
        for (size_t i=0; i<in_size; ++i){
            if(i == in.size()-1){
                std::cout<<in[i]<<"]";
            }else{
                std::cout<<in[i]<<", ";
            }
        }
    }
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
