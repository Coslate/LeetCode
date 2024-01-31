from typing import Optional, List
import collections
import math

class Solution:
    def transpose(self, matrix: List[List[int]], row_num: int) -> None:
        for i in range(row_num):
            for j in range(i+1, row_num):
                (matrix[i][j], matrix[j][i]) = (matrix[j][i], matrix[i][j])

    def reverse(self, matrix: List[List[int]], row_num: int) -> None:
        for i in range(row_num):
            for j in range(row_num//2):
                (matrix[i][j], matrix[i][row_num-j-1]) = (matrix[i][row_num-j-1], matrix[i][j])

    def rotate(self, matrix: List[List[int]]) -> None:
        # Matrix | Time: O(n^2) | Space: O(1)
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_num = len(matrix)
        self.transpose(matrix, row_num)
        self.reverse(matrix, row_num)

class OptSolution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Matrix | Time: O(n^2) | Space: O(1)
        """
        Do not return anything, modify matrix in-place instead.
        """
        pass
