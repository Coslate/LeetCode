#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    n = 5 
    edges = [[0,1],[0,2],[0,3],[1,4]]
    print(f"//------Original-------//")
    print(f"n = {n}, edges = {edges}")
    print(f"//------Checked-------//")
    output = sol.validTree(n, edges)
    output_opt = sol_opt.validTree(n, edges)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    print(f"//Case1:")
    n = 5
    edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    print(f"//------Original-------//")
    print(f"n = {n}, edges = {edges}")
    print(f"//------Checked-------//")
    output = sol.validTree(n, edges)
    output_opt = sol_opt.validTree(n, edges)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
