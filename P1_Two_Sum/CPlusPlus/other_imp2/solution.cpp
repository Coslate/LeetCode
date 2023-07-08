#include <map>
#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <solution.h>

/*
std::vector<int> Solution::twoSum(std::vector<int>& nums, int target) {
    std::map<int, int> hash_map;
    std::vector<int>::iterator vec_begin = nums.begin();
    std::vector<int>::iterator vec_end = nums.end();

    for (auto it = vec_begin; it != vec_end; ++it){
        int complement = target - *it;

        if (hash_map.find(complement)!=hash_map.end()) {
            std::vector<int> answer_vec (2, 0);
            answer_vec[0] = hash_map.find(complement)->second;
            answer_vec[1] = it - vec_begin;
            return answer_vec;
        }else{
            hash_map[*it] = it - vec_begin;
        }
    }

    printf("Error: No two sum solution.\n");
    exit (EXIT_FAILURE);
}
*/
std::vector<int> Solution::twoSum(std::vector<int>& nums, int target) {
    // Two Pointers Implementation | Time: O(nlogn) | Space: O(n)
    std::vector<int> answer_vec (2, 0);
    std::vector<std::pair<int, int>> result; //(num, index) tuple
    bool got_answer = false;

    //sorting
    for (size_t i=0, vec_size=nums.size(); i!=vec_size; ++i){
        std::pair<int, int> pair_idx = std::make_pair(nums[i], (int)i);
        result.push_back(pair_idx);
    }

    std::sort(result.begin(), result.end(), 
    [](const auto& a, const auto& b){return a.first < b.first;});

    //two pointers
    int i = 0;
    int j = nums.size()-1;

    while(i<j){
        if(result[i].first + result[j].first == target){
            answer_vec[0] = result[i].second;
            answer_vec[1] = result[j].second;
            got_answer = true;
            break;
        }else if(result[i].first + result[j].first < target){//too small, ++i
            ++i;
        }else{//too large, --j
            --j;
        }
    }

    if(!got_answer){
        printf("Error: No two sum solution.\n");
        exit (EXIT_FAILURE);
    }
    return answer_vec;
}
