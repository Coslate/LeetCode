#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    tasks = ["A","A","A","B","B","B"]
    n = 2
    ans = Solution().leastInterval(tasks, n)
    print(f"ans = {ans}")

    print(f"//Case2:")
    tasks = ["A","C","A","B","D","B"]
    n = 1
    ans = Solution().leastInterval(tasks, n)
    print(f"ans = {ans}")

    print(f"//Case3:")
    tasks = ["A","A","A", "B","B","B"]
    n = 3
    ans = Solution().leastInterval(tasks, n)
    print(f"ans = {ans}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
