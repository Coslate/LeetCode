#include <solution.h>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <numeric>
#include <unordered_map>

uint32_t Solution::reverseNBits(uint32_t n, uint32_t k){
    int result = 0;
    int power = k-1;

    while( n != 0){
        result += (n & 1) << power;
        n = n >> 1;
        power -= 1;

    }

    return result;
}

uint32_t Solution::reverseBits(uint32_t n){
    //Bit Operation | Time: O(1) | Space: O(1), n is the input length of array
    std::unordered_map<int, int> cache;
    uint32_t k_bits = 8;
    uint32_t mask = 0;
    uint32_t shift_bits = 0;
    uint32_t power = 32 - k_bits;
    uint32_t result = 0;

    while (shift_bits < k_bits){
        mask += 1 << shift_bits;
        shift_bits++;
    }

    while (n != 0){
        uint32_t least_bits = n & mask;
        uint32_t reversed_bits = 0;

        if(cache.find(least_bits) != cache.end()){
            reversed_bits = cache[least_bits];
        }else{
            reversed_bits = reverseNBits(least_bits, k_bits);
            cache[least_bits] = reversed_bits;
        }
        result += reversed_bits << power;
        n = n >> k_bits;
        power -= k_bits;
    }

    return result;
}

uint32_t OptSolution::reverseBits(uint32_t n){
    //Bit Operation | Time: O(n) | Space: O(1), n is the input length of array
    Solution sol;
    return sol.reverseBits(n);
}

