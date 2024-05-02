#include <solution.h>
#include <climits>
#include <cmath>

#include <cstdlib>

std::vector<int> Solution::countBits(int n){
    //Bit Operation | Dynamic Programming | Time: O(1) | Space: O(1), n is the input number
    std::vector<int> result(n+1, 0); 
    for(int i=1; i<n+1; ++i){
        //P(x) = P(x/2) + (x mod 2)
        result[i] = result[i>>1] + (i & 1);
    }

    return result;
}

std::vector<int> OptSolution::countBits(int n){
    //Bit Operation | Dynamic Programming | Time: O(1) | Space: O(1), n is the input number
    Solution sol;
    return sol.countBits(n);
}

