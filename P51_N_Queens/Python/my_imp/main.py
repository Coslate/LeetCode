#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    n = 4
    ans = Solution().solveNQueens(n)
    print(f"ans = {ans}")

    print(f"//Case2:")
    n = 1
    ans = Solution().solveNQueens(n)
    print(f"ans = {ans}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
