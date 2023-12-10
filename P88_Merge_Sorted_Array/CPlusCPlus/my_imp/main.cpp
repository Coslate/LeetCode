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
    std::vector<int> nums1 = {1, 2, 3, 0, 0, 0};
    std::vector<int> nums2 = {2, 5, 6};
    int m=3;
    int n=3;
    Solution sol;
    OptSolution opt_sol;

    std::cout<<"//Case1:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"nums1 = "<<nums1<<std::endl;
    std::cout<<"nums2 = "<<nums2<<std::endl;
    std::cout<<"//-----Merged-----//"<<std::endl;
    //sol.merge(nums1, m, nums2, n);
    opt_sol.merge(nums1, m, nums2, n);
    std::cout<<"nums1 = "<<nums1<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    nums1 = {1};
    m = 1;
    nums2 = {};
    n = 0;
    std::cout<<"//Case2:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"nums1 = "<<nums1<<std::endl;
    std::cout<<"nums2 = "<<nums2<<std::endl;
    std::cout<<"//-----Merged-----//"<<std::endl;
    //sol.merge(nums1, m, nums2, n);
    opt_sol.merge(nums1, m, nums2, n);
    std::cout<<"nums1 = "<<nums1<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    nums1 = {0};
    m = 0;
    nums2 = {1};
    n = 1;
    std::cout<<"//Case3:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"nums1 = "<<nums1<<std::endl;
    std::cout<<"nums2 = "<<nums2<<std::endl;
    std::cout<<"//-----Merged-----//"<<std::endl;
    //sol.merge(nums1, m, nums2, n);
    opt_sol.merge(nums1, m, nums2, n);
    std::cout<<"nums1 = "<<nums1<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    nums1 = {4, 5, 6, 0, 0, 0};
    m = 3;
    nums2 = {1, 2, 3};
    n = 3;
    std::cout<<"//Case4:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"nums1 = "<<nums1<<std::endl;
    std::cout<<"nums2 = "<<nums2<<std::endl;
    std::cout<<"//-----Merged-----//"<<std::endl;
    //sol.merge(nums1, m, nums2, n);
    opt_sol.merge(nums1, m, nums2, n);
    std::cout<<"nums1 = "<<nums1<<std::endl;
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
