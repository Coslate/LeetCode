#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    piles = [3,6,7,11]
    h = 8
    ans = Solution().minEatingSpeed(piles, h)
    print(f"ans = {ans}")

    print(f"//Case2:")
    piles = [30,11,23,4,20]
    h = 5
    ans = Solution().minEatingSpeed(piles, h)
    print(f"ans = {ans}")

    print(f"//Case3:")
    piles = [30,11,23,4,20]
    h = 6
    ans = Solution().minEatingSpeed(piles, h)
    print(f"ans = {ans}")




#---------------Execution---------------#
if __name__ == '__main__':
    main()
