#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(f"//------Original-------//")
    print(f"strs = {strs}")
    print(f"//------Checked-------//")
    output = sol.groupAnagrams(strs)
    print(f"output = {output}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    strs = [""]
    print(f"//------Original-------//")
    print(f"strs = {strs}")
    print(f"//------Checked-------//")
    output = sol.groupAnagrams(strs)
    print(f"output = {output}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    strs = ["a"]
    print(f"//------Original-------//")
    print(f"strs = {strs}")
    print(f"//------Checked-------//")
    output = sol.groupAnagrams(strs)
    print(f"output = {output}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
