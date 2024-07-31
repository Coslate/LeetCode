#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    s = "ADOBECODEBANC"; t = "ABC"
    print(f"//------Original-------//")
    print(f"s = {s}, t = {t}")
    print(f"//------Checked-------//")
    output = sol.minWindow(s, t)
    output_opt = sol_opt.minWindow(s, t)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    s = "a"; t = "a"
    print(f"//------Original-------//")
    print(f"s = {s}, t = {t}")
    print(f"//------Checked-------//")
    output = sol.minWindow(s, t)
    output_opt = sol_opt.minWindow(s, t)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    print(f"//Case3:")
    s = "a"; t = "aa"
    print(f"//------Original-------//")
    print(f"s = {s}, t = {t}")
    print(f"//------Checked-------//")
    output = sol.minWindow(s, t)
    output_opt = sol_opt.minWindow(s, t)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")



#---------------Execution---------------#
if __name__ == '__main__':
    main()
