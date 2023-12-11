#include <solution.h>

bool Solution::isSubsequence(std::string s, std::string t) {
    //Time: O(n) | Space: O(1), m is the size of s, n is the size of t
    int start_index = 0;
    int end_index = (int)t.size();
    bool ans = true;

    for(size_t i=0; i<s.size(); ++i){
        bool ele_s_exist = false;

        for(int j=start_index; j<end_index; ++j){
            if(t[j] == s[i]){
                ele_s_exist = true;
                start_index = j+1;
                break;
            }
        }

        if(!ele_s_exist){
            ans = false;
            break;
        }
    }
    return ans;
}

bool OptSolution::isSubsequence(std::string s, std::string t) {
    // Two Pointers | Time: O(n) | Space: O(1), n is the size of t
    int n = (int)t.size();
    int m = (int)s.size();
    int s_ptr = 0;
    bool ans = false;

    for(int t_ptr = 0; s_ptr < m && t_ptr < n; ++t_ptr){
        if(s[s_ptr] == t[t_ptr]){
            s_ptr++;
        }
    }
    if(s_ptr == m){
        ans = true;
    }

    return ans;
}

