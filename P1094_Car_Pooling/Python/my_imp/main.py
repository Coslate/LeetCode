#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    trips = [[2,1,5],[3,3,7]]
    capacity = 4
    print(f"ans = {Solution().carPooling(trips, capacity)}")

    print(f"//Case2:")
    trips = [[2,1,5],[3,3,7]]
    capacity = 5
    print(f"ans = {Solution().carPooling(trips, capacity)}")

    print(f"//Case3:")
    trips = [[2,1,5],[3,5,7]]
    capacity = 3
    print(f"ans = {Solution().carPooling(trips, capacity)}")

    print(f"//Case4:")
    trips = [[9,3,6],[8,1,7],[6,6,8],[8,4,9],[4,2,9]]
    capacity = 28
    print(f"ans = {Solution().carPooling(trips, capacity)}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
