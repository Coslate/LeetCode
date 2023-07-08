#include <iostream>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <vector>
#include <solution.h>

int main(){
    //Declare final solution container.
    std::vector<int> final_answer;

    //The input testing arguments.
    int target = 9;
    int myints[] = {2, 7, 11, 5};
    std::vector<int> nums(myints, myints+sizeof(myints)/sizeof(int));

    //Calculation body
    Solution sol_obj;
    final_answer = sol_obj.twoSum(nums, target);

    //Print the result.
    for (auto it = final_answer.begin(), end = final_answer.end(); it != end; ++it){
        if(it==final_answer.begin()){
            printf("answer = [%d", *it);
        }else if(it==end-1){
            printf(", %d]\n", *it);
        }else{
            printf(", %d", *it);
        }
    }

    return EXIT_SUCCESS;
}
