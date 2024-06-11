#include <solution.h>
#include <cmath>
#include <cstdlib>
#include <climits>

void Solution::printArray(const int* const &in, std::string name, const int in_size){
    std::cout<<name<<" = "<<"[";
    for (int i=0; i<in_size; ++i){
        if(i == in_size-1){
            std::cout<<in[i]<<"]"<<std::endl;
        }else{
            std::cout<<in[i]<<", ";
        }
    }

}

int Solution::coinChange(std::vector<int>& coins, int amount) {
    //Dynamic Programming | Time: O(n) | Space: O(n), n is the input length of coins
    //P(n) = min(P(n-c)+1, P(n)), foreach c in coins.
    int *dp = new int [amount+1] ();
    std::fill_n(dp, amount+1, INT_MAX);
    dp[0] = 0;
    int ans = 0;

    for(size_t coin_index=0; coin_index < coins.size(); ++coin_index){
        for(int i=coins[coin_index]; i < amount+1; ++i){
            int result = (dp[i-coins[coin_index]] == INT_MAX) ? INT_MAX : dp[i-coins[coin_index]] + 1; //prevent overflow
            dp[i] = std::min(result, dp[i]);
        }
    }

    if (dp[amount] < INT_MAX){
        ans = dp[amount];
    }else{
        ans = -1;
    }

    delete [] dp;
    return ans;
}

int OptSolution::coinChange(std::vector<int>& coins, int amount) {
    //Dynamic Programming | Time: O(1) | Space: O(1), n is the input length of array
    //P(n) = min(P(n-c)+1, P(n)), foreach c in coins.

    Solution sol;
    return sol.coinChange(coins, amount);
}


