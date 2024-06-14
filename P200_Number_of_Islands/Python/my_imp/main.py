#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"grid = {grid}")
    print(f"//------Checked-------//")
    output = sol.numIslands(grid)
    output_opt = sol_opt.numIslands(grid)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"grid = {grid}")
    print(f"//------Checked-------//")
    output = sol.numIslands(grid)
    output_opt = sol_opt.numIslands(grid)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")





#---------------Execution---------------#
if __name__ == '__main__':
    main()
