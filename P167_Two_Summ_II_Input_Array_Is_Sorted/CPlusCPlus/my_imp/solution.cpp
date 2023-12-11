#include <solution.h>

std::vector<int> Solution::twoSum(std::vector<int>& numbers, int target){
    //Two Pointers | Time: O(n) | Space: O(1), n is the size of numbers
    int ptr_l = 0;
    int ptr_r = (int)numbers.size() - 1;
    std::vector<int> result;

    while(ptr_l < ptr_r){
        if(numbers[ptr_l] + numbers[ptr_r] > target){
            ptr_r--;
        }else if(numbers[ptr_l] + numbers[ptr_r] < target){
            ptr_l++;
        }else{
            result.push_back(ptr_l+1);
            result.push_back(ptr_r+1);
            break;
        }
    }

    return result;
}

std::vector<int> OptSolution::twoSum(std::vector<int>& numbers, int target){
    //Two Pointers | Time: O(n) | Space: O(1), n is the size of numbers
    // Same as the twoSum() in Solution class (above).
    Solution sol;
    return sol.twoSum(numbers, target);
}

