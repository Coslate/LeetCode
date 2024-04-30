#include <solution.h>
#include <climits>
#include <cmath>

#include <cstdlib>

int Solution::hammingWeight(int n){
    //Bit Operation | Time: O(1) | Space: O(1), n is the input number
    int result = 0;
    int mask   = 1;

    for(int i = 0; i < 32; ++i){
        if((n & mask) != 0){
            result += 1;
        }
        mask = mask << 1;
    }

    return result;
}

int OptSolution::hammingWeight(int n){
    //Bit Operation | Time: O(1) | Space: O(1), n is the size of input array
    Solution sol;
    return sol.hammingWeight(n);
}

