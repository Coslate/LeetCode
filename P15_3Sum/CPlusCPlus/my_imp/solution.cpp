#include <map>
#include <vector>
#include <cstdio>
#include <solution.h>
#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>


std::vector<std::vector<int>> Solution::threeSum(std::vector<int>& nums){
    // Two Pointers | Time: O(nlogn+n^2) | Space: O(1) (Do not consider
    // answer storing and output)
    std::vector<std::vector<int>> ans;
    std::vector<int> nums_sorted = nums;

    //Sort the nums
    std::sort(nums_sorted.begin(), nums_sorted.end());//Remove repeated triplets.

    for(size_t i=0; i<nums_sorted.size(); ++i){
        if(i && nums_sorted[i] == nums_sorted[i-1]) continue; //Remove repeated triplets.
        size_t j = i+1;
        size_t k = nums_sorted.size()-1;

        while(j < k){
            if(nums_sorted[i] + nums_sorted[j] + nums_sorted[k] > 0) --k;
            else if(nums_sorted[i] + nums_sorted[j] + nums_sorted[k] < 0) ++j;
            else{
                ans.push_back(std::vector<int>{nums_sorted[i], nums_sorted[j], nums_sorted[k]});
                while(j < k && nums_sorted[j]==nums_sorted[j+1]) ++j;//Remove repeated triplets.
                while(j < k && nums_sorted[k]==nums_sorted[k-1]) --k;//Remove repeated triplets.
                ++j;
                --k;
            }
        }
    }

    return ans;
}
