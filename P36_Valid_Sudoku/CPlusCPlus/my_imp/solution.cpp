#include <solution.h>

int Solution::atMost(std::vector<int>& nums, int k){
    if(k < 0){
        return 0;
    }

    int i = 0;
    int ans = 0;
    int num_size = (int)nums.size();

    for(int j = 0; j < num_size; ++j){
        k -= nums[j];
        while(k < 0){
            k += nums[i];
            i++;
        }
        ans += (j-i+1);
    }
    return ans;
}
int Solution::numSubarraysWithSum(std::vector<int>& nums, int goal){
    //Sliding Window | Time: O(n) | Space: O(1), n is the size of nums
    return atMost(nums, goal) - atMost(nums, goal-1);
}

int OptSolution::numSubarraysWithSum(std::vector<int>& nums, int goal){
    //Sliding Window | Time: O(n) | Space: O(1), n is the size of nums
    Solution sol;
    return sol.numSubarraysWithSum(nums, goal);
}

