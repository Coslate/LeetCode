#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1
    print(f"ans = {Solution().findCheapestPrice(n, flights, src, dst, k)}")

    print(f"//Case2:")
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    print(f"ans = {Solution().findCheapestPrice(n, flights, src, dst, k)}")

    print(f"//Case3:")
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 0
    print(f"ans = {Solution().findCheapestPrice(n, flights, src, dst, k)}")

    print(f"//Case4:")
    n = 10
    flights = [[0,1,20],[1,2,20],[2,3,30],[3,4,30],[4,5,30],[5,6,30],[6,7,30],[7,8,30],[8,9,30],[0,2,9999],[2,4,9998],[4,7,9997]]
    src = 0
    dst = 9
    k = 4
    print(f"ans = {Solution().findCheapestPrice(n, flights, src, dst, k)}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
