#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    intervals = [[0,30],[5,10],[15,20]]
    print(f"//------Original-------//")
    print(f"intervals = {intervals}")
    print(f"//------Checked-------//")
    output = sol.canAttendMeetings(intervals)
    #output_opt = sol_opt.countComponents(n, edges)
    print(f"output = {output}")
    #print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    intervals = [[7,10],[2,4]]
    print(f"//------Original-------//")
    print(f"intervals = {intervals}")
    print(f"//------Checked-------//")
    output = sol.canAttendMeetings(intervals)
    #output_opt = sol_opt.countComponents(n, edges)
    print(f"output = {output}")
    #print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")



#---------------Execution---------------#
if __name__ == '__main__':
    main()
