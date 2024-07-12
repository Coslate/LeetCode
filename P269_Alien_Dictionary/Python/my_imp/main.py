#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    words = ['wrt', 'wrf', 'er', 'ett', 'rftt']
    print(f"//------Original-------//")
    print(f"words = {words}")
    print(f"//------Checked-------//")
    output = sol.alienOrder(words)
    #output_opt = sol_opt.numIslands(grid)
    print(f"output = {output}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    words = ['z', 'x']
    print(f"//------Original-------//")
    print(f"words = {words}")
    print(f"//------Checked-------//")
    output = sol.alienOrder(words)
    #output_opt = sol_opt.numIslands(grid)
    print(f"output = {output}")
    print(f"")
    print(f"")

    print(f"//Case3:")
    words = ['z', 'x', 'z']
    print(f"//------Original-------//")
    print(f"words = {words}")
    print(f"//------Checked-------//")
    output = sol.alienOrder(words)
    #output_opt = sol_opt.numIslands(grid)
    print(f"output = {output}")
    print(f"")
    print(f"")

    print(f"//Case4:")
    words = ['ab', 'abcd']
    print(f"//------Original-------//")
    print(f"words = {words}")
    print(f"//------Checked-------//")
    output = sol.alienOrder(words)
    #output_opt = sol_opt.numIslands(grid)
    print(f"output = {output}")
    print(f"")
    print(f"")

    print(f"//Case5:")
    words = ['abcd', 'ab']
    print(f"//------Original-------//")
    print(f"words = {words}")
    print(f"//------Checked-------//")
    output = sol.alienOrder(words)
    #output_opt = sol_opt.numIslands(grid)
    print(f"output = {output}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
