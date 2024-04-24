#include <solution.h>
#include <climits>
#include <cmath>

int Solution::findMinPtr(std::vector<int>& nums){
    //Array | Binary Search | Time: O(logn) | Space: O(1), n is the size of input array
    int left_ptr = 0;
    int right_ptr = int(nums.size())-1;

    if(left_ptr == right_ptr){
        return left_ptr;
    }

    if(nums[left_ptr] < nums[right_ptr]){
        return left_ptr;
    }

    while(left_ptr < right_ptr){
        int mid_ptr = std::ceil((left_ptr+right_ptr)/2.f);

        if(nums[mid_ptr-1] > nums[mid_ptr]){
            return mid_ptr;
        }else if(nums[left_ptr] < nums[mid_ptr]){
            left_ptr = mid_ptr;
        }else{
            right_ptr = mid_ptr;
        }
    }

    return -1;
}

int Solution::binSearch(int left_ptr, int right_ptr, std::vector<int>& nums, const int target){
    if(left_ptr == right_ptr){
        if(target == nums[left_ptr]){
            return left_ptr;
        }else{
            return -1;
        }
    }

    while(left_ptr <= right_ptr){
        int mid_ptr = int((left_ptr+right_ptr)/2);

        if(target == nums[mid_ptr]){
            return mid_ptr;
        }else if(target > nums[mid_ptr]){
            left_ptr = mid_ptr +1;
        }else{
            right_ptr = mid_ptr-1;
        }
    }
    return -1;
}

int Solution::search(std::vector<int>& nums, int target){
    int min_ptr = findMinPtr(nums);
    int nums_length = int(nums.size());

    if(min_ptr == 0){
        return binSearch(0, nums_length-1, nums, target);
    }else{
        if(nums[0] == target){
            return 0;
        }else if(nums[0] < target){
            return binSearch(0, min_ptr-1, nums, target);
        }else{
            return binSearch(min_ptr, nums_length-1, nums, target);
        }
    }

    return -1;
}

int OptSolution::search(std::vector<int>& nums, int target){
    //Array | Binary Search | Time: O(logn) | Space: O(1), n is the size of input array
    //Combine inflection point and binary search into one binary search.
    int n = nums.size();
    int left_ptr = 0;
    int right_ptr = n-1;

    while(left_ptr <= right_ptr){
        int mid_ptr = int((left_ptr + right_ptr)/2);

        if(nums[mid_ptr] == target){//Case1
            return mid_ptr;
        }else if(nums[left_ptr] <= nums[mid_ptr]){//Case2: left part is a sorted array
            if(target >= nums[left_ptr] && target < nums[mid_ptr]){//if target is in the range of left sorted array
                right_ptr = mid_ptr-1;
            }else{
                left_ptr = mid_ptr+1;
            }
        }else{//Case3: right part is a sorted array
            if(target > nums[mid_ptr] && target <= nums[right_ptr]){//if target is in the range of right sorted array
                left_ptr = mid_ptr+1;
            }else{
                right_ptr = mid_ptr-1;
            }
        }
    }

    return -1;
}

