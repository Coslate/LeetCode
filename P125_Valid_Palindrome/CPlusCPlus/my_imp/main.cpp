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
    bool k = false;

    std::string s = "A man, a plan, a canal: Panama";
    std::cout<<"//Case1:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"s = "<<s<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    //k = sol.isPalindrome(s);
    k = opt_sol.isPalindrome(s);
    std::cout<<"k = "<<k<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    s = "race a car";
    std::cout<<"//Case2:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"s = "<<s<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    //k = sol.isPalindrome(s);
    k = opt_sol.isPalindrome(s);
    std::cout<<"k = "<<k<<std::endl;
    std::cout<<std::endl;
    std::cout<<std::endl;

    s = " ";
    std::cout<<"//Case3:"<<std::endl;
    std::cout<<"//-----Original-----//"<<std::endl;
    std::cout<<"s = "<<s<<std::endl;
    std::cout<<"//-----Checked-----//"<<std::endl;
    //k = sol.isPalindrome(s);
    k = opt_sol.isPalindrome(s);
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
