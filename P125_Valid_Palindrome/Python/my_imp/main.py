#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    s = "A man, a plan, a canal: Panama"
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"s = {s}")

    print(f"//------Checked-------//")
    ans = sol.isPalindrome(s)
    print(f"ans = {ans}")
    print(f"")
    print(f"")

    s = "race a car"
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"s = {s}")

    print(f"//------Checked-------//")
    ans = sol.isPalindrome(s)
    print(f"ans = {ans}")
    print(f"")
    print(f"")

    s = " "
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"s = {s}")

    print(f"//------Checked-------//")
    ans = sol.isPalindrome(s)
    print(f"ans = {ans}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
