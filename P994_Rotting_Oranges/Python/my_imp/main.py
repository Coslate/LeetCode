#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    ans = Solution().orangesRotting(grid)
    print(f"ans = {ans}")

    print(f"//Case2:")
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    ans = Solution().orangesRotting(grid)
    print(f"ans = {ans}")

    print(f"//Case3:")
    grid = [[0,2]]
    ans = Solution().orangesRotting(grid)
    print(f"ans = {ans}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
