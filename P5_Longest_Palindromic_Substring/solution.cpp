#include <map>
#include <vector>
#include <cstdio>
#include <solution.h>
#include <cstring>
#include <string>
#include <iostream>

#define MAX_IN_STRLEN 1000

void Solution::swap(char& ch_a, char& ch_b){
    char tmp = ch_a;
    ch_a = ch_b;
    ch_b = tmp;
}

void Solution::reverseStrRef(std::string &str){ 
    int n = str.length(); 
  
    // Swap character starting from two 
    // corners 
    for (int i = 0; i < n / 2; i++) 
        swap(str[i], str[n - i - 1]); 
}

std::string Solution::reverseStrCpy(const std::string &str){ 
    std::string rev_str = str;
    int n = str.size();

    // Swap character starting from two 
    // corners 
    for (int i = 0; i < n / 2; i++) 
        swap(rev_str[i], rev_str[n - i - 1]); 

    return(rev_str);
}

//Brute Force
/*
std::string Solution::longestPalindrome(std::string s){
    int max_pal_size = 0;
    std::string s_ans;

    for(int i=0;i<s.size();++i){
        for(int j=0;j<s.size();++j){
            std::string s_ans_tmp = "";
            int start_idx = i;
            int end_idx = (i+j > s.size()) ? (s.size()-1) : (i+j);

            for(int k=start_idx;k<=end_idx;++k){
                s_ans_tmp.push_back(s[k]);
            }

            if((s_ans_tmp.compare(reverseStrCpy(s_ans_tmp)) == 0) && (s_ans_tmp.size() > max_pal_size)){
                max_pal_size = s_ans_tmp.size();
                s_ans = s_ans_tmp;
            }
        }
    }

    return s_ans;
}
*/

//Dynamic Programming
std::string Solution::longestPalindrome(std::string str){
    int str_size = str.size();
    int ** ans_idx_arr = new int* [str_size]();
    for(int i=0;i<str_size;++i){
        ans_idx_arr[i] = new int [str_size]();
    }

    for(int i=0;i<str_size;++i){
        std::cout<<"i = "<<i<<", ";
        for(int j=0;j<str_size;++j){
            std::cout<<"ans_idx_arr["<<i<<"]["<<j<<"] = "<<ans_idx_arr[i][j]<<", ";
        }
        std::cout<<std::endl;
    }

    return "test";
}
