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
    int ans = -1;
    int ans_opt = -1;

    std::vector<int> numbers1 = {4, 5, 6, 7, 0, 1, 2};
    int target = 0;
    std::cout<<"//Case1:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"numbers1 = "<<numbers1<<std::endl;
    std::cout<<"target = "<<target<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans     = sol.search(numbers1, target);
    ans_opt     = opt_sol.search(numbers1, target);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<"ans_opt = "<<ans_opt<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    std::vector<int> numbers2 = {4, 5, 6, 7, 0, 1, 2};
    target = 3;
    std::cout<<"//Case2:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"numbers2 = "<<numbers2<<std::endl;
    std::cout<<"target = "<<target<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans     = sol.search(numbers2, target);
    ans_opt     = opt_sol.search(numbers2, target);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<"ans_opt = "<<ans_opt<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    std::vector<int> numbers3 = {1};
    target = 0;
    std::cout<<"//Case3:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"numbers3 = "<<numbers3<<std::endl;
    std::cout<<"target = "<<target<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans     = sol.search(numbers3, target);
    ans_opt     = opt_sol.search(numbers3, target);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<"ans_opt = "<<ans_opt<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    std::vector<int> numbers4 = {1, 3};
    target = 3;
    std::cout<<"//Case4:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"numbers4 = "<<numbers4<<std::endl;
    std::cout<<"target = "<<target<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans     = sol.search(numbers4, target);
    ans_opt     = opt_sol.search(numbers4, target);
    std::cout<<"ans = "<<ans<<std::endl;
    std::cout<<"ans_opt = "<<ans_opt<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    std::vector<int> numbers5 = {3, 1};
    target = 3;
    std::cout<<"//Case5:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"numbers5 = "<<numbers5<<std::endl;
    std::cout<<"target = "<<target<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    ans     = sol.search(numbers5, target);
    ans_opt     = opt_sol.search(numbers5, target);
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
