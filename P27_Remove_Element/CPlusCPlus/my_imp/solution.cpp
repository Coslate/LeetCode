#include <solution.h>

int Solution::removeElement(std::vector<int>& nums, int val) {
    // Time: O(n) | Space: O(n)
    std::vector<int> result_arr;

    for(size_t i=0; i < nums.size(); ++i){
        if(nums[i] != val){
            result_arr.push_back(nums[i]);
        }
    }
    nums.assign(result_arr.begin(), result_arr.end());
    return nums.size();
}

int OptSolution::removeElement(std::vector<int>& nums, int val) {
    // Time: O(n) | Space: O(1)
    int mod_index = 0;

    for(size_t i=0; i < nums.size(); ++i){
        if(nums[i] != val){
            nums[mod_index] = nums[i];
            mod_index++;
        }
    }
    return mod_index;
}
