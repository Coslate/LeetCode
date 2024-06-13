#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"heights = {heights}")
    print(f"//------Checked-------//")
    output = sol.pacificAtlantic(heights)
    print(f"output = {output}")
    print(f"")
    print(f"")

    heights = [[1]]
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"heights = {heights}")
    print(f"//------Checked-------//")
    output = sol.pacificAtlantic(heights)
    print(f"output = {output}")
    print(f"")
    print(f"")

    heights = [[2, 1], [1, 2]]
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"heights = {heights}")
    print(f"//------Checked-------//")
    output = sol.pacificAtlantic(heights)
    print(f"output = {output}")
    print(f"")
    print(f"")



#---------------Execution---------------#
if __name__ == '__main__':
    main()
