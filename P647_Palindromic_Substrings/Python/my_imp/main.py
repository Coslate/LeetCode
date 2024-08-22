#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    s = "abc"
    print(f"//------Original-------//")
    print(f"s = {s}")
    print(f"//------Checked-------//")
    output = sol.countSubstrings(s)
    print(f"output = {output}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    s = "aaa"
    print(f"//------Original-------//")
    print(f"s = {s}")
    print(f"//------Checked-------//")
    output = sol.countSubstrings(s)
    print(f"output = {output}")
    print(f"")
    print(f"")



#---------------Execution---------------#
if __name__ == '__main__':
    main()
