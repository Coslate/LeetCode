#include <iostream>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <vector>
#include <solution.h>
#include <cstring>

int main(){
    //Declare final solution container.
    std::string input_s = "abcabcbb";

    //Calculation body
    Solution sol_obj;
    int s_max_len = sol_obj.lengthOfLongestSubstring(input_s);

    //Print the result.
    std::cout<<"input_s = "<<input_s<<std::endl;
    std::cout<<"The maximum non-repeated length of the sub-string is = "<<s_max_len<<std::endl;

    return EXIT_SUCCESS;
}
