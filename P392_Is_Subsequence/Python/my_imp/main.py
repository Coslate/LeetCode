#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    s = "abc"
    t = "ahbgdc"
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"s = {s}")
    print(f"t = {t}")

    print(f"//------Checked-------//")
    ans = sol.isSubsequence(s, t)
    print(f"ans = {ans}")
    print(f"")
    print(f"")

    s = "axc"
    t = "ahbgdc"
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"s = {s}")
    print(f"t = {t}")

    print(f"//------Checked-------//")
    ans = sol.isSubsequence(s, t)
    print(f"ans = {ans}")
    print(f"")
    print(f"")

    s = "acb"
    t = "ahbgdc"
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"s = {s}")
    print(f"t = {t}")

    print(f"//------Checked-------//")
    ans = sol.isSubsequence(s, t)
    print(f"ans = {ans}")
    print(f"")
    print(f"")

    s = "aaaaaa"
    t = "bbaaaa"
    print(f"//Case4:")
    print(f"//------Original-------//")
    print(f"s = {s}")
    print(f"t = {t}")

    print(f"//------Checked-------//")
    ans = sol.isSubsequence(s, t)
    print(f"ans = {ans}")
    print(f"")
    print(f"")




#---------------Execution---------------#
if __name__ == '__main__':
    main()
