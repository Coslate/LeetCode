#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    points = [[10,16],[2,8],[1,6],[7,12]]
    print(f"ans = {Solution().findMinArrowShots(points)}")

    print(f"//Case2:")
    points = [[1,2],[3,4],[5,6],[7,8]]
    print(f"ans = {Solution().findMinArrowShots(points)}")

    print(f"//Case3:")
    points = [[1,2],[2,3],[3,4],[4,5]]
    print(f"ans = {Solution().findMinArrowShots(points)}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
