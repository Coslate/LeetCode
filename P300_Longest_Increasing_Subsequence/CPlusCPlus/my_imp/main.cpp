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
    int ans = -1, ans_opt = -1;

    std::vector<int> nums = {10,9,2,5,3,7,101,18};
    std::cout<<"//Case1:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"nums = "<<nums<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.lengthOfLIS(nums);
    ans_opt = sol_opt.lengthOfLIS(nums);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<"ans_opt = "<<ans_opt<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    std::vector<int> nums2 = {0, 1, 0, 3, 2, 3};
    std::cout<<"//Case2:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"nums2 = "<<nums2<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.lengthOfLIS(nums2);
    ans_opt = sol_opt.lengthOfLIS(nums2);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<"ans_opt = "<<ans_opt<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    std::vector<int> nums3 = {7,7,7,7,7,7,7};
    std::cout<<"//Case3:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"nums3 = "<<nums3<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.lengthOfLIS(nums3);
    ans_opt = sol_opt.lengthOfLIS(nums3);
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
