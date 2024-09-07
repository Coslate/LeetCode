#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    haystack = "sadbutsad"; needle = "sad"
    print(f"//------Original-------//")
    print(f"haystack = {haystack}, needle = {needle}")
    print(f"//------Checked-------//")
    output = sol.strStr(haystack, needle)
    print(f"output = {output}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    haystack = "leetcode"; needle = "leeto"
    print(f"//------Original-------//")
    print(f"haystack = {haystack}, needle = {needle}")
    print(f"//------Checked-------//")
    output = sol.strStr(haystack, needle)
    print(f"output = {output}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
