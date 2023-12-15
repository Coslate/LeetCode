#include <solution.h>

int Solution::atMost(std::vector<int> &nums, int k){
    int i = 0;
    int num_of_subarray = 0;

    for(int j = 0; j < (int)nums.size(); ++j){
        k -= (nums[j]%2);
        while( k < 0 ){
            k += (nums[i]%2);
            i++;
        }
        num_of_subarray += j-i+1;
    }
    return num_of_subarray;
}

int Solution::numberOfSubarrays(std::vector<int>& nums, int k){
    //Sliding Window | Time: O(n) | Space: O(1), n is the size of nums
    return atMost(nums, k) - atMost(nums, (k-1));
}

int OptSolution::numberOfSubarrays(std::vector<int>& nums, int k){
    //Sliding Window | Time: O(n) | Space: O(1), n is the size of nums
    // Same as the twoSum() in Solution class (above).
    Solution sol;
    return sol.numberOfSubarrays(nums, k);
}

