#include <solution.h>
#include <cmath>
#include <cstdlib>
#include <climits>

void Solution::printArray(const std::vector<int> &in, std::string name){
    std::cout<<name<<" = "<<"[";
    for (size_t i=0; i<in.size(); ++i){
        if(i == in.size()-1){
            std::cout<<in[i]<<"]"<<std::endl;
        }else{
            std::cout<<in[i]<<", ";
        }
    }

}

void Solution::printArray(const int* const &in, std::string name, const int in_size){
    std::cout<<name<<" = "<<"[";
    for (int i=0; i<in_size; ++i){
        if(i == in_size-1){
            std::cout<<in[i]<<"]"<<std::endl;
        }else{
            std::cout<<in[i]<<", ";
        }
    }

}

int Solution::lengthOfLIS(std::vector<int>& nums){
    //Dynamic Programming | Time: O(n^2) | Space: O(n), n is the input length of nums
    //P(i) = max(P(j)+1, P(i)) foreach nums[j] < nums[i] and j < i
    int *dp = new int [nums.size()] ();
    std::fill_n(dp, nums.size(), 1);
    int max_result = -1;

    for(size_t i=0; i < nums.size(); ++i){
        for(size_t j=0; j < i; ++j){
            dp[i] = (nums[j] < nums[i]) ? std::max(dp[j]+1, dp[i]) : dp[i];
        }
        max_result = std::max(max_result, dp[i]);
    }

    delete [] dp;
    return max_result;
}

int OptSolution::binarySearch(const std::vector<int>& nums, const int target){
    int left = 0;
    int right = int(nums.size())-1;
    int res = -1;

    while(left <= right){
        int mid = std::floor((left+right)/2);
        if(target > nums[mid]){
            left = mid+1;
            res = mid+1;
        }else if(target < nums[mid]){
            right = mid-1;
            res = mid;
        }else{
            res = mid;
            break;
        }
    }

    return res;
}

int OptSolution::lengthOfLIS(std::vector<int>& nums){
    //Binary Search | Time: O(nlogn) | Space: O(n), n is the input length of nums
    std::vector<int> constructed_optsol = {nums[0]};
    for(size_t i=1; i < nums.size(); ++i){
        if (constructed_optsol.back() < nums[i]){
            constructed_optsol.push_back(nums[i]);
        }else{
            int inserted_pos = binarySearch(constructed_optsol, nums[i]);
            constructed_optsol[inserted_pos] = nums[i];
        }
    }

    return int(constructed_optsol.size());
}

