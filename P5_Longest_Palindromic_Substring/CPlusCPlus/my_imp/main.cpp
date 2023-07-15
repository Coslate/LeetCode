#include <iostream>
#include <cstdlib>
#include <climits>
#include <vector>
#include <solution.h>
#include <cstring>
#include <string>

int main(){
    //Declare final solution container.
    std::string input_s = "babad";

    //Calculation body
    Solution sol_obj;
    std::string s_max_pal = sol_obj.longestPalindrome(input_s);

    //Print the result.
    std::cout<<"input_s = "<<input_s<<std::endl;
    std::cout<<"The maximum palindrome is = "<<s_max_pal<<std::endl;

    return EXIT_SUCCESS;
}
