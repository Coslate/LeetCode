#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    s = "anagram"; t = "nagaram"
    print(f"//------Original-------//")
    print(f"s = {s}, t = {t}")
    print(f"//------Checked-------//")
    output = sol.isAnagram(s, t)
    print(f"output = {output}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    s = "rat"; t = "car"
    print(f"//------Original-------//")
    print(f"s = {s}, t = {t}")
    print(f"//------Checked-------//")
    output = sol.isAnagram(s, t)
    print(f"output = {output}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
