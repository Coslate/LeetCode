#include <solution.h>
#include <unordered_map>

std::vector<int> Solution::productExceptSelf(std::vector<int>& nums){
    // Array | Time: O(n) | Space: O(1), n is the size of prices[]
    OptSolution sol_opt;
    return sol_opt.productExceptSelf(nums);
}

std::vector<int> OptSolution::productExceptSelf(std::vector<int>& nums){
    // Array | Time: O(n) | Space: O(1), n is the size of prices[]
    std::vector<int> answer;
    int left_prod = 1;
    int right_prod = 1;
    int nums_size = (int)nums.size();

    answer.push_back(1);
    for(int i=1; i<nums_size; ++i){
        left_prod *= nums[i-1];
        answer.push_back(left_prod);
    }


    for(int i=nums_size-2; i > -1; --i){
        right_prod *= nums[i+1];
        answer[i] *= right_prod;
    }

    return answer;
}


