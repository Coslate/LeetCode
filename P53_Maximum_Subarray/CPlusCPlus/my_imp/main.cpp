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
    int ans, ans_opt;

    std::vector<int> numbers = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    std::cout<<"//Case1:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"numbers = "<<numbers<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans     = sol.maxSubArray(numbers);
    ans_opt = opt_sol.maxSubArray(numbers);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<"ans_opt = "<<ans_opt<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    std::vector<int> numbers2 = {1};
    std::cout<<"//Case2:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"numbers2 = "<<numbers2<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans     = sol.maxSubArray(numbers2);
    ans_opt = opt_sol.maxSubArray(numbers2);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<"ans_opt = "<<ans_opt<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    std::vector<int> numbers3 = {5, 4, -1, 7, 8};
    std::cout<<"//Case3:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"numbers3 = "<<numbers3<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans     = sol.maxSubArray(numbers3);
    ans_opt = opt_sol.maxSubArray(numbers3);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<"ans_opt = "<<ans_opt<<std::endl;
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
