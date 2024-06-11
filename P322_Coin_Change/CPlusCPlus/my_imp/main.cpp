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
    OptSolution sol_opt;
    int ans = -1;

    std::vector<int> coins = {1, 2, 5};
    int amount = 11;
    std::cout<<"//Case1:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"coins = "<<coins<<std::endl;
    std::cout<<"amount = "<<amount<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.coinChange(coins, amount);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    std::vector<int> coins2 = {2};
    int amount2 = 3;
    std::cout<<"//Case2:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"coins2 = "<<coins2<<std::endl;
    std::cout<<"amount2 = "<<amount2<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.coinChange(coins2, amount2);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    std::vector<int> coins3 = {1};
    int amount3 = 0;
    std::cout<<"//Case3:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"coins3 = "<<coins3<<std::endl;
    std::cout<<"amount3 = "<<amount3<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.coinChange(coins3, amount3);
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
