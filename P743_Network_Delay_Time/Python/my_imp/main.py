#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2
    print(f"ans = {Solution().networkDelayTime(times, n, k)}")

    print(f"//Case2:")
    times = [[1,2,1]]
    n = 2
    k = 1
    print(f"ans = {Solution().networkDelayTime(times, n, k)}")

    print(f"//Case3:")
    times = [[1,2,1]]
    n = 2
    k = 2
    print(f"ans = {Solution().networkDelayTime(times, n, k)}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
