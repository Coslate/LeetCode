#include <solution.h>
#include <climits>

int Solution::maxSubArrayRangeSearch(const int left_idx, const int right_idx, const std::vector<int> &nums){
    if(left_idx > right_idx){
        return -INT_MAX;
    }

    int left_pos_max = 1;
    int left_neg_max = 1;
    int right_pos_max = 1;
    int right_neg_max = 1;
    int mid_sum_max = 1;
    int mid_idx = (int)(left_idx + right_idx)/2;

    //left sum max
    int cur_sum = 1;
    for(int i=mid_idx-1; i >= left_idx; --i){
        cur_sum *= nums[i];
        left_pos_max = std::max(left_pos_max, cur_sum);
        left_neg_max = std::min(left_neg_max, cur_sum);
    }

    //right sum max
    cur_sum = 1;
    for(int i=mid_idx+1; i <= right_idx; ++i){
        cur_sum *= nums[i];
        right_pos_max = std::max(right_pos_max, cur_sum);
        right_neg_max = std::min(right_neg_max, cur_sum);
    }

    if(nums[mid_idx] > 0){
        mid_sum_max = std::max(nums[mid_idx] * left_pos_max * right_pos_max, nums[mid_idx] * left_neg_max * right_neg_max);
    }else{
        mid_sum_max = std::max(nums[mid_idx] * left_pos_max * right_neg_max, nums[mid_idx] * left_neg_max * right_pos_max);
    }

    int left_sum_range_max  = maxSubArrayRangeSearch(left_idx, mid_idx-1, nums);
    int right_sum_range_max = maxSubArrayRangeSearch(mid_idx+1, right_idx, nums);

    return std::max(std::max(mid_sum_max, left_sum_range_max), right_sum_range_max);
}

int Solution::maxProduct(std::vector<int>& nums){
    //Array | Divida and Conquer | Time: O(nlogn) | Space: O(logn), n is the size of input array
    return maxSubArrayRangeSearch(0, nums.size()-1, nums);
}

int OptSolution::maxProduct(std::vector<int>& nums){
    //Array | Divida and Conquer | Time: O(nlogn) | Space: O(logn), n is the size of input array
    int max_so_far = nums[0];
    int min_so_far = nums[0];
    int result     = nums[0];

    for(int i = 1; i < (int)nums.size(); ++i){
        int cur_max = std::max(nums[i], std::max(max_so_far*nums[i], min_so_far*nums[i]));
        min_so_far = std::min(nums[i], std::min(max_so_far*nums[i], min_so_far*nums[i]));
        max_so_far = cur_max;

        result = std::max(result, max_so_far);
    }

    return result;
}

