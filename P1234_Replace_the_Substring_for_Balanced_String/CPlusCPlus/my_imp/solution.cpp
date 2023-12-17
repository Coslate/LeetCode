#include <solution.h>

int Solution::balancedString(std::string s){
    //Sliding Window | Time: O(n) | Space: O(n), n is the size of nums
    std::unordered_map<std::string, int> count;
    int s_size = (int)s.size();
    int ans_num = s_size;
    int avg_thr = s_size/4;
    int i = 0;

    for(int j=0; j<s_size; ++j){
        std::string single_str_s(1, s[j]);

        if(count.find(single_str_s) == count.end()){//not found
            count[single_str_s] = 1;
        }else{
            count[single_str_s]++;
        }
    }

    std::cout<<"count['Q'] = "<<count["Q"]<<std::endl;
    std::cout<<"count['R'] = "<<count["R"]<<std::endl;
    std::cout<<"count['W'] = "<<count["W"]<<std::endl;
    std::cout<<"count['E'] = "<<count["E"]<<std::endl;

    for(int j=0; j<s_size; ++j){
        std::string single_str_j(1, s[j]);
        count[single_str_j]--;
        while( (i<s_size) && (count["Q"] <= avg_thr) && (count["R"] <= avg_thr) && (count["W"] <= avg_thr) && (count["E"] <= avg_thr)){
            std::string single_str_i(1, s[i]);
            ans_num = std::min(ans_num, j-i+1);
            count[single_str_i]++;
            i++;
        }
    }

    return ans_num;
}

int OptSolution::balancedString(std::string s){
    //Sliding Window | Time: O(n) | Space: O(n), n is the size of nums
    // Same as the twoSum() in Solution class (above).
    Solution sol;
    return sol.balancedString(s);
}

