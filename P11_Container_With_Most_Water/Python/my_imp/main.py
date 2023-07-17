#! /usr/bin/env python3

from solution import Solution

def main():
    sol = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    ans = sol.maxArea(height)
    print(f"height = {height}")
    print(f"ans = {ans}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
