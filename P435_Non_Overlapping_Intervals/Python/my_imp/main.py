#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    print(f"//------Original-------//")
    print(f"intervals = {intervals}")
    print(f"//------Checked-------//")
    output = sol.eraseOverlapIntervals(intervals)
    #output_opt = sol_opt.countComponents(n, edges)
    print(f"output = {output}")
    #print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    intervals = [[1,2],[1,2],[1,2]]
    print(f"//------Original-------//")
    print(f"intervals = {intervals}")
    print(f"//------Checked-------//")
    output = sol.eraseOverlapIntervals(intervals)
    #output_opt = sol_opt.countComponents(n, edges)
    print(f"output = {output}")
    #print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    print(f"//Case3:")
    intervals = [[1,2],[2,3]]
    print(f"//------Original-------//")
    print(f"intervals = {intervals}")
    print(f"//------Checked-------//")
    output = sol.eraseOverlapIntervals(intervals)
    #output_opt = sol_opt.countComponents(n, edges)
    print(f"output = {output}")
    #print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")



#---------------Execution---------------#
if __name__ == '__main__':
    main()
