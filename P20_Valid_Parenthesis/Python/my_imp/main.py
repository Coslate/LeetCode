#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    s = "()"
    print(f"//------Original-------//")
    print(f"s = {s}")
    print(f"//------Checked-------//")
    output = sol.isValid(s)
    print(f"output = {output}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    s = "()[]{}"
    print(f"//------Original-------//")
    print(f"s = {s}")
    print(f"//------Checked-------//")
    output = sol.isValid(s)
    print(f"output = {output}")
    print(f"")
    print(f"")

    print(f"//Case3:")
    s = "(]"
    print(f"//------Original-------//")
    print(f"s = {s}")
    print(f"//------Checked-------//")
    output = sol.isValid(s)
    print(f"output = {output}")
    print(f"")
    print(f"")

    print(f"//Case4:")
    s = "["
    print(f"//------Original-------//")
    print(f"s = {s}")
    print(f"//------Checked-------//")
    output = sol.isValid(s)
    print(f"output = {output}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
