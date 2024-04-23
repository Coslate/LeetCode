#include <solution.h>
#include <climits>
#include <cmath>

int Solution::findMin(std::vector<int>& nums){
    //Array | Binary Search | Time: O(logn) | Space: O(1), n is the size of input array
    int left_ptr = 0;
    int right_ptr = int(nums.size())-1;

    if(left_ptr == right_ptr){
        return nums[left_ptr];
    }

    if(nums[left_ptr] < nums[right_ptr]){
        return nums[left_ptr];
    }

    while(left_ptr < right_ptr){
        int mid_ptr = std::ceil((left_ptr+right_ptr)/2.f);

        if(nums[mid_ptr-1] > nums[mid_ptr]){
            return nums[mid_ptr];
        }else if(nums[left_ptr] < nums[mid_ptr]){
            left_ptr = mid_ptr;
        }else{
            right_ptr = mid_ptr;
        }
    }

    return -INT_MAX;
}

int OptSolution::findMin(std::vector<int>& nums){
    //Array | Binary Search | Time: O(logn) | Space: O(1), n is the size of input array
    Solution sol;
    return sol.findMin(nums);
}

