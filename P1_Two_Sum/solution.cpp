#include <map>
#include <vector>
#include <cstdio>
#include <solution.h>

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
