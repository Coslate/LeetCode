#include <solution.h>

bool Solution::isPalindrome(std::string s) {
    // Time: O(n) | Space: O(n)
    std::string alnum_list;
    std::string alnum_list_inv;
    bool ans = true;
    size_t s_size = s.size();
    size_t alnum_size = 0;

    if(int(s_size) == 0){
        return true;
    }

    for(size_t i=0; i<s_size; ++i){
        if(isalnum(s[i])){
            alnum_list.push_back(tolower(s[i]));
        }
    }
    alnum_size = alnum_list.size();

    for(int i=(int)alnum_size-1; i>=0; --i){
        alnum_list_inv.push_back(alnum_list[i]);
    }

    ans = !alnum_list.compare(alnum_list_inv);
    return ans;
}

bool OptSolution::isPalindrome(std::string s) {
    // Time: O(n) | Space: O(1)
    int s_length = s.size();
    if(s_length == 0){
        return true;
    }

    int ptr_l = 0;
    int ptr_r = s_length-1;
    int ans = true;

    while(ptr_l <= ptr_r){
        if(!isalnum(s[ptr_l])){
            ptr_l++;
        }else if(!isalnum(s[ptr_r])){
            ptr_r--;
        }else{
            if(tolower(s[ptr_l]) != tolower(s[ptr_r])){
                ans = false;
                break;
            }else{
                ptr_l++;
                ptr_r--;
            }
        }
    }

    return ans;
}

