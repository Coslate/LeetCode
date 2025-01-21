#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    s = "aa"
    p = "a"
    print(f"ans = {Solution().isMatch(s, p)}")

    print(f"//Case2:")
    s = "aa"
    p = "a*"
    print(f"ans = {Solution().isMatch(s, p)}")

    print(f"//Case3:")
    s = "ab"
    p = ".*"
    print(f"ans = {Solution().isMatch(s, p)}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
