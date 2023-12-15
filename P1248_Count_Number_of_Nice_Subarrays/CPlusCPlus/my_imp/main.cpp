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

    std::vector<int> numbers = {1, 1, 2, 1, 1};
    int k = 3;
    std::cout<<"//Case1:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"numbers = "<<numbers<<std::endl;
    std::cout<<"k = "<<k<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.numberOfSubarrays(numbers, k);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    numbers = {2, 4, 6};
    k = 1;
    std::cout<<"//Case2:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"numbers = "<<numbers<<std::endl;
    std::cout<<"k = "<<k<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.numberOfSubarrays(numbers, k);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    numbers = {2, 2, 2, 1, 2, 2, 1, 2, 2, 2};
    k = 2;
    std::cout<<"//Case3:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"numbers = "<<numbers<<std::endl;
    std::cout<<"k = "<<k<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans = sol.numberOfSubarrays(numbers, k);
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
