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
    std::vector<int> nums = {3, 2, 2, 3};
    int val=3;
    int k=-1;
    Solution sol;
    OptSolution opt_sol;

    std::cout<<"//Case1:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"nums = "<<nums<<std::endl;
    std::cout<<"val = "<<val<<std::endl;
    std::cout<<"//-----Merged-----//"<<std::endl;
    //k = sol.removeElement(nums, val);
    k = opt_sol.removeElement(nums, val);
    std::cout<<"nums = "<<nums<<std::endl;
    std::cout<<"k = "<<k<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    nums = {0, 1, 2, 2, 3, 0, 4, 2};
    val=2;
    std::cout<<"//Case1:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"nums = "<<nums<<std::endl;
    std::cout<<"val = "<<val<<std::endl;
    std::cout<<"//-----Merged-----//"<<std::endl;
    //k = sol.removeElement(nums, val);
    k = opt_sol.removeElement(nums, val);
    std::cout<<"nums = "<<nums<<std::endl;
    std::cout<<"k = "<<k<<std::endl;
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
