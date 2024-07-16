#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    n = 5
    edges = [[0,1],[1,2],[3,4]]
    print(f"//------Original-------//")
    print(f"n = {n}, edges = {edges}")
    print(f"//------Checked-------//")
    output = sol.countComponents(n, edges)
    output_opt = sol_opt.countComponents(n, edges)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    n = 5
    edges = [[0,1],[1,2],[2,3],[3,4]]
    print(f"//------Original-------//")
    print(f"n = {n}, edges = {edges}")
    print(f"//------Checked-------//")
    output = sol.countComponents(n, edges)
    output_opt = sol_opt.countComponents(n, edges)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    print(f"//Case3:")
    n = 4
    edges = [[2,3],[1,2],[1,3]]
    print(f"//------Original-------//")
    print(f"n = {n}, edges = {edges}")
    print(f"//------Checked-------//")
    output = sol.countComponents(n, edges)
    output_opt = sol_opt.countComponents(n, edges)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
