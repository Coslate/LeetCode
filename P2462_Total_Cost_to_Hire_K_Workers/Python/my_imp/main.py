#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    costs = [17,12,10,2,7,2,11,20,8]
    k = 3
    candidates = 4
    print(f"ans = {Solution().totalCost(costs, k, candidates)}")

    print(f"//Case2:")
    costs = [1,2,4,1]
    k = 3
    candidates = 3
    print(f"ans = {Solution().totalCost(costs, k, candidates)}")

    print(f"//Case3:")
    costs = [10,1,11,10]
    k = 2
    candidates = 1
    print(f"ans = {Solution().totalCost(costs, k, candidates)}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
