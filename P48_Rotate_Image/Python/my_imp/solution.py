from typing import Optional, List
import collections
import math

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Matrix | Time: O(n^2) | Space: O(1)
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_num = len(matrix)
        col_num = len(matrix[0])
        iter_num = math.ceil(row_num/2)
        iter_index = 0
        iterloop_index_i = 0
        iterloop_index_j = 0

        while(iter_index < iter_num):
            pass



class OptSolution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Matrix | Time: O(n^2) | Space: O(1)
        """
        Do not return anything, modify matrix in-place instead.
        """
        pass
