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
    std::vector<int> nums = {1, 0, 1, 0, 1};
    int goal = 2;

    std::cout<<"//Case1:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"nums = "<<nums<<std::endl;
    std::cout<<"goal = "<<goal<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.numSubarraysWithSum(nums, goal);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    nums = {0, 0, 0, 0, 0};
    goal = 0;
    std::cout<<"//Case2:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"nums = "<<nums<<std::endl;
    std::cout<<"goal = "<<goal<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.numSubarraysWithSum(nums, goal);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    nums = {0, 1, 1, 1, 1};
    goal = 3;
    std::cout<<"//Case2:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"nums = "<<nums<<std::endl;
    std::cout<<"goal = "<<goal<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.numSubarraysWithSum(nums, goal);
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
