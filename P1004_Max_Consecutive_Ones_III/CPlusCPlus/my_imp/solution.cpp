#include <solution.h>

int Solution::longestOnes(std::vector<int>& nums, int k){
    //Sliding Window | Time: O(n) | Space: O(1), n is the size of nums
    int i = 0;
    int ans = -1;
    int num_size = (int)nums.size();

    for(int j = 0; j < num_size; ++j){
        k -= 1-nums[j];

        while(k < 0){
            ans = std::max(ans, j-i);
            k += 1-nums[i];
            ++i;
        }

        if(j == num_size-1){
            ans = std::max(ans, j-i+1);
        }
    }

    return ans;
}

int OptSolution::longestOnes(std::vector<int>& nums, int k){
    //Sliding Window | Time: O(n) | Space: O(1), n is the size of nums
    int i = 0;
    int j = 0;
    int num_size = (int)nums.size();

    for(j = 0; j < num_size; ++j){
        k -= (1-nums[j]);
        if(k < 0){
            k += (1-nums[i]);
            ++i;
        }
    }

    return j-i;
}

