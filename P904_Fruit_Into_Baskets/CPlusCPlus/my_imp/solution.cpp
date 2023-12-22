#include <solution.h>

int Solution::totalFruit(std::vector<int>& fruits){
    //Sliding Window | Time: O(n) | Space: O(1), n is the size of nums
    int basket0  = -1;
    int basket1  = -1;
    int b1_ptr   = 0;
    int b0_ptr   = 0;
    int ans      = 0;
    int cur_size = 0;
    int fruit_size = (int)fruits.size();

    for(int j = 0; j < fruit_size; ++j){
        if(basket0 == -1 && basket1 == -1){
            basket0 = fruits[j];
            cur_size++;
            b0_ptr = j;
        }else if(basket0 == -1 && fruits[j] != basket1){
            basket0 = fruits[j];
            cur_size++;
            b0_ptr = j;
        }else if(basket1 == -1 && fruits[j] != basket0){
            basket1 = fruits[j];
            cur_size++;
            b1_ptr = j;
        }else{
            if(fruits[j] == basket0){
                cur_size++;
                if(fruits[j-1] != fruits[j]){
                    b0_ptr = j;
                }
            }else if(fruits[j] == basket1){
                cur_size++;
                if(fruits[j-1] != fruits[j]){
                    b1_ptr = j;
                }
            }else{
                if(basket0 == fruits[j-1]){
                    basket1 = fruits[j];
                    b1_ptr = j;
                }else{
                    basket0 = fruits[j];
                    b0_ptr = j;
                }
                ans = std::max(ans, cur_size);
                cur_size = abs(b0_ptr-b1_ptr)+1;
            }
        }
    }

    ans = std::max(ans, cur_size);
    return ans;
}

int OptSolution::totalFruit(std::vector<int>& fruits){
    //Sliding Window | Time: O(n) | Space: O(1), n is the size of nums
    Solution sol;
    return sol.totalFruit(fruits);
}

