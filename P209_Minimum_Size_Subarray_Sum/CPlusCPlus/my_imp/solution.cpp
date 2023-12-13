#include <solution.h>

int Solution::minSubArrayLen(int target, std::vector<int>& nums){
    //Sliding Window | Time: O(n) | Space: O(1), n is the size of nums
    int nums_size = nums.size();
    int ans_num   = nums_size;
    bool got_once = false;
    int  j        = 0;

    for(int i=0; i<nums_size; ++i){
        target -= nums[i];

        while(target <= 0){
            got_once = true;
            ans_num = std::min(ans_num, i-j+1);
            target += nums[j];
            ++j;
        }
    }

    return got_once ? ans_num : 0;
}


int OptSolution::minSubArrayLen(int target, std::vector<int>& nums){
    //Sliding Window | Time: O(n) | Space: O(1), n is the size of nums
    // Same as the twoSum() in Solution class (above).
    Solution sol;
    return sol.minSubArrayLen(target, nums);
}

