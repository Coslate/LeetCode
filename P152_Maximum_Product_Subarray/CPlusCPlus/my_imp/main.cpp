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

    std::vector<int> numbers = {2, 3, -2, 4};
    std::cout<<"//Case1:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"numbers = "<<numbers<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans     = sol.maxProduct(numbers);
    ans_opt = opt_sol.maxProduct(numbers);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<"ans_opt = "<<ans_opt<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    std::vector<int> numbers2 = {-2, 0, -1};
    std::cout<<"//Case2:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"numbers2 = "<<numbers2<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans     = sol.maxProduct(numbers2);
    ans_opt = opt_sol.maxProduct(numbers2);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<"ans_opt = "<<ans_opt<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    std::vector<int> numbers3 = {3, -1, 4};
    std::cout<<"//Case3:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"numbers3 = "<<numbers3<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans     = sol.maxProduct(numbers3);
    ans_opt = opt_sol.maxProduct(numbers3);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<"ans_opt = "<<ans_opt<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    std::vector<int> numbers4 = {2, -5, -2, -4, 3};
    std::cout<<"//Case4:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"numbers4 = "<<numbers4<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans     = sol.maxProduct(numbers4);
    ans_opt = opt_sol.maxProduct(numbers4);
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
