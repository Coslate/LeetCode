#include <solution.h>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <numeric>

int Solution::missingNumber(std::vector<int>& nums){
    //Bit Operation | Time: O(n) | Space: O(1), n is the input length of array
    int mem_ones[10000] = {0};

    for(int i=0; i<int(nums.size()); ++i){
        mem_ones[nums[i]] = 1;
    }
    for(int i=0; i<int(nums.size())+1; ++i){
        if(mem_ones[i] == 0){
            return i;
        }
    }
    return -1;
}

int OptSolution::missingNumber(std::vector<int>& nums){
    //Bit Operation | Time: O(n) | Space: O(1), n is the input length of array
    int nums_size = int(nums.size());
    int expected_sum = floor(((nums_size+1)*nums_size)/2);
    int actual_sum = std::accumulate(nums.begin(), nums.end(), 0);

    return expected_sum - actual_sum;
}

