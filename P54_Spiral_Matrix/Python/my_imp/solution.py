from typing import Optional, List
import collections

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Matrix | Time: O(n^2) | Space: O(1)
        index_i = 0
        index_j = 0
        row_num = len(matrix)
        col_num = len(matrix[0])
        count = 0
        total_element = row_num*col_num
        go_row = True
        go_col = False
        go_inc = True
        go_dec = False
        incr_cnt = 0
        decr_cnt = 0
        anchor_left  = 0
        anchor_right = col_num - 1
        anchor_up    = 1
        anchor_down  = row_num - 1
        ans_list = []

        while(count < total_element):
            '''
            print(f"ans_list = {ans_list}")
            print(f"--------------")
            print(f"count = {count}")
            print(f"go_row = {go_row}")
            print(f"go_col = {go_col}")
            print(f"go_inc = {go_inc}")
            print(f"go_dec = {go_dec}")
            '''

            if(go_row):
                if(go_inc):
                    while(index_j <= anchor_right):
                        ans_list.append(matrix[index_i][index_j])
                        index_j  += 1
                        count    += 1
                    index_j      -= 1
                    index_i      += 1
                    anchor_right -= 1
                    incr_cnt     += 1
                    if(incr_cnt == 2):
                        incr_cnt = 0
                        go_inc = False
                        go_dec = True
                elif(go_dec):
                    while(index_j >= anchor_left):
                        ans_list.append(matrix[index_i][index_j])
                        index_j -= 1
                        count   += 1
                    index_j     += 1
                    index_i     -= 1
                    anchor_left += 1
                    decr_cnt    += 1
                    if(decr_cnt == 2):
                        decr_cnt = 0
                        go_inc = True
                        go_dec = False
                go_row = False
                go_col = True

            '''
            print(f"ans_list = {ans_list}")
            print(f"--------------")
            print(f"count = {count}")
            print(f"go_row = {go_row}")
            print(f"go_col = {go_col}")
            print(f"go_inc = {go_inc}")
            print(f"go_dec = {go_dec}")
            '''

            if(go_col):
                if(go_inc):
                    while(index_i <= anchor_down):
                        ans_list.append(matrix[index_i][index_j])
                        index_i += 1
                        count += 1
                    index_i     -= 1
                    index_j     -= 1
                    anchor_down -= 1
                    incr_cnt += 1
                    if(incr_cnt == 2):
                        incr_cnt = 0
                        go_inc = False
                        go_dec = True
                elif(go_dec):
                    while(index_i >= anchor_up):
                        ans_list.append(matrix[index_i][index_j])
                        index_i -= 1
                        count   += 1
                    index_i     += 1
                    index_j     += 1
                    anchor_up   += 1
                    decr_cnt    += 1
                    if(decr_cnt == 2):
                        decr_cnt = 0
                        go_inc = True
                        go_dec = False
                go_row = True
                go_col = False

        return ans_list

class OptSolution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Matrix | Time: O(n^2) | Space: O(n^2)
        pass
