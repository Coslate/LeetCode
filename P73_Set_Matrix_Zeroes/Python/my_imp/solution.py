from typing import Optional, List
import collections

class Solution:
    def getBits(self, num: int, bit_reg: int) -> int:
        return bit_reg >> num & 1

    def setRowZeroes(self, index_i: int, col_num: int, matrix: List[List[int]]) -> None:
        for j in range(col_num):
            matrix[index_i][j] = 0

    def setColZeroes(self, index_j: int, row_num: int, matrix: List[List[int]]) -> None:
        for i in range(row_num):
            matrix[i][index_j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Matrix | Time: O(n^2) | Space: O(n^2)
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_num = len(matrix)
        col_num = len(matrix[0])
        bit_reg = 0
        for i in range(row_num):
            for j in range(col_num):
                if matrix[i][j] == 0:
                    num = i*col_num + j
                    bit_reg |= 1 << num

        for i in range(row_num):
            for j in range(col_num):
                num = i*col_num + j
                if (self.getBits(num, bit_reg)) == 1:
                    self.setRowZeroes(i, col_num, matrix)
                    self.setColZeroes(j, row_num, matrix)

class OptSolution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Matrix | Time: O(n^2) | Space: O(1)
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_set_zeroes = False
        first_col_set_zeroes = False
        row_num = len(matrix)
        col_num = len(matrix[0])

        for i in range(row_num):
            for j in range(col_num):
                if matrix[i][j] == 0:
                    if i == 0 :
                        first_row_set_zeroes = True
                    if j == 0:
                        first_col_set_zeroes = True

                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, row_num):
            for j in range(1, col_num):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if first_row_set_zeroes:
            for j in range(col_num):
                matrix[0][j] = 0

        if first_col_set_zeroes:
            for i in range(row_num):
                matrix[i][0] = 0


