#include <solution.h>

std::vector<int> Solution::spiralOrder(std::vector<std::vector<int>>& matrix){
    //Matrix | Time: O(n^2) | Space: O(1), n is the height or width of the matrix
    int index_i = 0;
    int index_j = 0;
    int row_num = matrix.size();
    int col_num = matrix[0].size();
    int count   = 0;
    int total_element = row_num*col_num;
    bool go_row = true;
    bool go_col = false;
    bool go_inc = true;
    bool go_dec = false;
    int incr_cnt = 0;
    int decr_cnt = 0;
    int anchor_left  = 0;
    int anchor_right = col_num - 1;
    int anchor_up    = 1;
    int anchor_down  = row_num - 1;
    std::vector<int> ans_list;

    while(count < total_element){
        if(go_row){
            if(go_inc){
                while(index_j <= anchor_right){
                    ans_list.push_back(matrix[index_i][index_j]);
                    index_j += 1;
                    count   += 1;
                }
                index_j      -= 1;
                index_i      += 1;
                anchor_right -= 1;
                incr_cnt     += 1;
                if(incr_cnt == 2){
                    incr_cnt = 0;
                    go_inc   = false;
                    go_dec   = true;
                }
            }else if(go_dec){
                while(index_j >= anchor_left){
                    ans_list.push_back(matrix[index_i][index_j]);
                    index_j -= 1;
                    count   += 1;
                }
                index_j     += 1;
                index_i     -= 1;
                anchor_left += 1;
                decr_cnt    += 1;
                if(decr_cnt == 2){
                    decr_cnt = 0;
                    go_inc   = true;
                    go_dec   = false;
                }
            }
            go_row = false;
            go_col = true;
        }

        if(go_col){
            if(go_inc){
                while(index_i <= anchor_down){
                    ans_list.push_back(matrix[index_i][index_j]);
                    index_i += 1;
                    count   += 1;
                }
                index_i     -= 1;
                index_j     -= 1;
                anchor_down -= 1;
                incr_cnt    += 1;
                if(incr_cnt == 2){
                    incr_cnt = 0;
                    go_inc   = false;
                    go_dec   = true;
                }
            }else if(go_dec){
                while(index_i >= anchor_up){
                    ans_list.push_back(matrix[index_i][index_j]);
                    index_i -= 1;
                    count   += 1;
                }
                index_i   += 1;
                index_j   += 1;
                anchor_up += 1;
                decr_cnt  += 1;
                if(decr_cnt == 2){
                    decr_cnt = 0;
                    go_inc   = true;
                    go_dec   = false;
                }
            }

            go_row = true;
            go_col = false;
        }
    }

    return ans_list;
}

std::vector<int> OptSolution::spiralOrder(std::vector<std::vector<int>>& matrix){
    //Matrix | Time: O(n^2) | Space: O(1), n is the height or width of the matrix
    std::vector<int> a;
    return a;
}

