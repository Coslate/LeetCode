#include <map>
#include <vector>
#include <cstdio>
#include <solution.h>
#include <cstring>
#include <string>

#define MAX_CHARS_NUM 128

int Solution::lengthOfLongestSubstring(std::string s){
    int max_len     = 0;
    int current_len = 1;
    int string_size = s.size();
    int prev_index  = 0;
    int *visited = new int [MAX_CHARS_NUM];
        
    if(string_size > 0){
        for(int i=0;i<MAX_CHARS_NUM;++i){
            visited[i] = -1;
        }
        visited[(int)s[0]] = 0;
    }
        
    for(int i=1;i<string_size;++i){
        prev_index = visited[(int)s[i]];
            
        if(prev_index == -1 || i-current_len > prev_index){
            ++current_len;
        }else{
            if(current_len > max_len){
                max_len = current_len;
            }
            current_len = i - prev_index;
        }
        
        visited[(int)s[i]] = i;
    }
        
    if((current_len > max_len) && (string_size > 0)){
        max_len = current_len;
    }
        
    delete [] visited;
    return max_len;    
}
