#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    print(f"ans = {Solution().longestIncreasingPath(matrix)}")

    print(f"//Case2:")
    matrix = [[3,4,5],[3,2,6],[2,2,1]]
    print(f"ans = {Solution().longestIncreasingPath(matrix)}")

    print(f"//Case3:")
    matrix = [[1]]
    print(f"ans = {Solution().longestIncreasingPath(matrix)}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
