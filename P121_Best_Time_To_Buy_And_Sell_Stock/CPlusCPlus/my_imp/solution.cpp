#include <solution.h>

int Solution::maxProfit(std::vector<int>& prices){
    // Array | Time: O(n) | Space: O(1), n is the size of prices[]
    int max_prof = 0;
    int record_min = prices[0];

    for(size_t i=0; i < prices.size(); ++i){
        if(prices[i] > record_min){
            max_prof = std::max(max_prof, prices[i] - record_min);
        }else{
            record_min = prices[i];
        }
    }

    return max_prof;
}

int OptSolution::maxProfit(std::vector<int>& prices){
    // Array | Time: O(n) | Space: O(1), n is the size of prices[]
    // Same as the maxProfit() in Solution class (above).
    Solution sol;
    return sol.maxProfit(prices);
}

