#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(f"ans = {Solution().searchMatrix(matrix, target)}")

    print(f"//Case2:")
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    print(f"ans = {Solution().searchMatrix(matrix, target)}")

    print(f"//Case3:")
    matrix = [[1, 1]]
    target = 0
    print(f"ans = {Solution().searchMatrix(matrix, target)}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
