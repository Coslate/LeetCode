#include <solution.h>
#include <climits>
#include <cmath>

#include <cstdlib>

int Solution::getSum(int a, int b){
    //Bit Operation | Time: O(1) | Space: O(1), n is the size of input array
    int x = abs(a);
    int y = abs(b);

    if(y > x) return getSum(b, a);

    int sign = (a >= 0) ? 1 : -1;

    if(a*b >= 0){
        while( y != 0){
            // x+y
            int add_wo_carry = x^y;
            int carry        = (x&y) << 1;
            x = add_wo_carry;
            y = carry;
        }
    }else{
        while( y != 0){
            // x-y
            int sub_wo_borrow = x^y;
            int borrow        = ((~x)&y) << 1;
            x = sub_wo_borrow;
            y = borrow;
        }
    }

    return sign*x;
}

int OptSolution::getSum(int a, int b){
    //Bit Operation | Time: O(1) | Space: O(1), n is the size of input array
    Solution sol;
    return sol.getSum(a, b);
}

