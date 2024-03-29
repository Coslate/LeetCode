#include <map>
#include <vector>
#include <cstdio>
#include <cstdlib>
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
    // Hash Table Implementation | Time: O(n) | Space: O(n)
    std::map<int, int> hash_map;
    std::vector<int> answer_vec (2, 0);
    bool got_answer = false;

    for (size_t i=0, vec_size=nums.size(); i!=vec_size; ++i){
        int complement = target - nums[i];

        if (hash_map.find(complement)!=hash_map.end()) {
            answer_vec[0] = hash_map.find(complement)->second;
            answer_vec[1] = i;
            got_answer = true;
        }else{
            hash_map[nums[i]] = i;
        }
    }

    if(!got_answer){
        printf("Error: No two sum solution.\n");
        exit (EXIT_FAILURE);
    }
    return answer_vec;
}
