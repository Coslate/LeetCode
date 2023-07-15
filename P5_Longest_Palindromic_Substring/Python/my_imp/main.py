#! /usr/bin/env python3

from solution import Solution

def main():
    sol = Solution()
    s = "babad"

    ans = sol.longestPalindrome(s)
    print(f"s = {s}")
    print(f"ans = {ans}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
