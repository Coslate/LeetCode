#include <solution.h>

int Solution::balancedString(std::string s){
    //Sliding Window | Time: O(n) | Space: O(1), n is the size of nums
    std::unordered_map<std::string, int> count;
    int s_size = (int)s.size();
    int ans_num = s_size;
    int avg_thr = s_size/4;
    int i = 0;

    for(int j=0; j<s_size; ++j){
        std::string single_str_s(1, s[j]);
        count[single_str_s]++;
    }

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
    //Sliding Window | Time: O(n) | Space: O(1), n is the size of nums
    std::unordered_map<int, int> count;
    int s_size = (int)s.size();
    int ans_num = s_size;
    int avg_thr = s_size/4;
    int i = 0;

    for(int j=0; j<s_size; ++j){
        count[s[j]]++;
    }

    for(int j=0; j<s_size; ++j){
        count[s[j]]--;
        while( (i<s_size) && (count['Q'] <= avg_thr) && (count['R'] <= avg_thr) && (count['W'] <= avg_thr) && (count['E'] <= avg_thr)){
            ans_num = std::min(ans_num, j-i+1);
            count[s[i++]]++;
        }
    }

    return ans_num;
}

