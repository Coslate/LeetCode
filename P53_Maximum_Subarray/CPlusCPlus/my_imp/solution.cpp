#include <solution.h>
#include <climits>

int Solution::maxSubArrayRangeSearch(const int left_idx, const int right_idx, const std::vector<int> &nums){
    if(left_idx > right_idx){
        return -INT_MAX;
    }

    int left_sum_max = 0;
    int right_sum_max = 0;
    int mid_sum_max = 0;
    int mid_idx = (int)(left_idx + right_idx)/2;

    //left sum max
    int cur_sum = 0;
    for(int i=mid_idx-1; i >= left_idx; --i){
        cur_sum += nums[i];
        left_sum_max = std::max(left_sum_max, cur_sum);
    }

    //right sum max
    cur_sum = 0;
    for(int i=mid_idx+1; i <= right_idx; ++i){
        cur_sum += nums[i];
        right_sum_max = std::max(right_sum_max, cur_sum);
    }

    mid_sum_max = nums[mid_idx] + left_sum_max + right_sum_max;

    int left_sum_range_max  = maxSubArrayRangeSearch(left_idx, mid_idx-1, nums);
    int right_sum_range_max = maxSubArrayRangeSearch(mid_idx+1, right_idx, nums);

    return std::max(std::max(mid_sum_max, left_sum_range_max), right_sum_range_max);
}

int Solution::maxSubArray(std::vector<int>& nums){
    //Array | Divida and Conquer | Time: O(nlogn) | Space: O(logn), n is the size of input array
    return maxSubArrayRangeSearch(0, nums.size()-1, nums);
}

int OptSolution::maxSubArray(std::vector<int>& nums){
    //Array | Divida and Conquer | Time: O(nlogn) | Space: O(logn), n is the size of input array
    int curr_pos_sum = nums[0];
    int max_sum      = curr_pos_sum;

    for(int i=1; i < int(nums.size()); ++i){
        curr_pos_sum = std::max(nums[i], nums[i] + curr_pos_sum);
        max_sum      = std::max(max_sum, curr_pos_sum);
    }

    return max_sum;
}

