#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    ans = Solution().trap_dynamic_programming(height)
    ans_two_ptr = Solution().trap(height)
    print(f"ans = {ans}")
    print(f"ans_two_ptr = {ans_two_ptr}")

    print(f"//Case2:")
    height = [4,2,0,3,2,5]
    ans = Solution().trap_dynamic_programming(height)
    ans_two_ptr = Solution().trap(height)
    print(f"ans = {ans}")
    print(f"ans_two_ptr = {ans_two_ptr}")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
