#include <solution.h>
#include <unordered_map>

bool Solution::containsDuplicate(std::vector<int>& nums){
    // Array | Time: O(n) | Space: O(1), n is the size of prices[]
    std::unordered_map<int, int> umap;

    for(auto num: nums){
        if(umap.find(num) == umap.end()){
            umap[num] = 1;
        }else{
            return true;
        }
    }

    return false;
}

bool OptSolution::containsDuplicate(std::vector<int>& nums){
    // Array | Time: O(n) | Space: O(1), n is the size of prices[]
    Solution sol;
    return sol.containsDuplicate(nums);
}


