#include <iostream>
#include <cstdlib>
#include <climits>
#include <vector>
#include <solution.h>
#include <cstring>
#include <string>

void printArray(const std::vector<int> &in, std::string name);
void printArray(const std::vector<std::vector<int>> &in, std::string name);
std::ostream & operator << (std::ostream &out, const std::vector<int> &in);

int main(){
    //Declare final solution container.
    std::vector<int> nums = {-1, 0, 1, 2, -1, -4};

    //Calculation body
    Solution sol_obj;
    std::vector<std::vector<int>> ans = sol_obj.threeSum(nums);

    //Print the result.
    printArray(nums, "nums");
    printArray(ans, "ans");

    return EXIT_SUCCESS;
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

void printArray(const std::vector<std::vector<int>> &in, std::string name){
    std::cout<<name<<" = "<<"[";
    for (size_t i=0; i<in.size(); ++i){
        if(i == in.size()-1){
            std::cout<<in[i]<<"]"<<std::endl;
        }else{
            std::cout<<in[i]<<", ";
        }
    }

}

std::ostream & operator << (std::ostream &out, const std::vector<int> &in){
    std::cout<<"[";
    for (size_t i=0; i<in.size(); ++i){
        if(i == in.size()-1){
            std::cout<<in[i]<<"]";
        }else{
            std::cout<<in[i]<<", ";
        }
    }
    return out;
}
