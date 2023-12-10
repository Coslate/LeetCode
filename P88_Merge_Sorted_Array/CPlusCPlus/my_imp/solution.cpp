#include <solution.h>

void Solution::merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n){
    //linear merge | Time: O(m+n) | Space: O(m+n)
    size_t ptr1 = 0;
    size_t ptr2 = 0;
    std::vector<int> result_arr;
    for(size_t i=0; i<nums1.size(); ++i){
        if(ptr1 == (size_t)m){
            result_arr.push_back(nums2[ptr2]);
            ptr2++;
        }else if(ptr2 == (size_t)n){
            result_arr.push_back(nums1[ptr1]);
            ptr1++;
        }else{
            if(nums2[ptr2] < nums1[ptr1]){
                result_arr.push_back(nums2[ptr2]);
                ptr2++;
            }else{
                result_arr.push_back(nums1[ptr1]);
                ptr1++;
            }
        }
    }
    nums1.assign(result_arr.begin(), result_arr.end());
}
void OptSolution::merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n){
    //linear merge | Time: O(m+n) | Space: O(1)
    int ptr1 = m-1;
    int ptr2 = n-1;
    int k    = m+n-1;

    while( ptr2 >= 0){
        if(ptr1 >=0 && nums1[ptr1] > nums2[ptr2]){
            nums1[k--] = nums1[ptr1--];
        }else{
            nums1[k--] = nums2[ptr2--];
        }
    }
}
