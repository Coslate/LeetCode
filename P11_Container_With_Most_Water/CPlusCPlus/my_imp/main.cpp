#include <iostream>
#include <cstdlib>
#include <climits>
#include <vector>
#include <solution.h>
#include <cstring>
#include <string>

int main(){
    //Declare final solution container.
    std::vector<int> height = {1, 8, 6, 2, 5, 4, 8, 3, 7};

    //Calculation body
    Solution sol_obj;
    int max_area = sol_obj.maxArea(height);

    //Print the result.
    std::cout<<"height = "<<"[";
    for (size_t i=0; i<height.size(); ++i){
        if(i == height.size()-1){
            std::cout<<height[i]<<"]"<<std::endl;
        }else{
            std::cout<<height[i]<<", ";
        }
    }
    std::cout<<"The maximum area is = "<<max_area<<std::endl;

    return EXIT_SUCCESS;
}
