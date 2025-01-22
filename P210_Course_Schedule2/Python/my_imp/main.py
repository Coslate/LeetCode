#! /usr/bin/env python3

from solution import *

def main():
    print(f"//Case1:")
    numCourses = 2
    prerequisites = [[1,0]]
    print(f"ans = {Solution().findOrder(numCourses, prerequisites)}")

    print(f"//Case2:")
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(f"ans = {Solution().findOrder(numCourses, prerequisites)}")

    print(f"//Case3:")
    numCourses = 1
    prerequisites = []
    print(f"ans = {Solution().findOrder(numCourses, prerequisites)}")

    print(f"//Case4:")
    numCourses = 2
    prerequisites = [[0, 1]]
    print(f"ans = {Solution().findOrder(numCourses, prerequisites)}")

    print(f"//Case5:")
    numCourses = 2
    prerequisites = [[0,1],[1,0]]
    print(f"ans = {Solution().findOrder(numCourses, prerequisites)}")



#---------------Execution---------------#
if __name__ == '__main__':
    main()
