#include <map>
#include <vector>
#include <cstdio>
#include <solution.h>
#include <cstring>
#include <string>
#include <iostream>

int Solution::maxArea(std::vector<int> &height){
    // Two Pointers | Time: O(n) | Space: O(1)
    int left = 0;
    int right = (int)height.size()-1;
    int max_area = -1;

    while(left < right){
        max_area = std::max(max_area, std::min(height[left], height[right])*(right-left));
        if(height[left] < height[right]){
            ++left;
        }else{
            --right;
        }
    }

    return max_area;
}
