#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    n = 3
    print(f"ans = {Solution().generateParenthesis(n)}")

    print(f"//Case2:")
    n = 1
    print(f"ans = {Solution().generateParenthesis(n)}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
