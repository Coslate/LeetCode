#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    s = "ABAB"; k = 2
    print(f"//------Original-------//")
    print(f"s = {s}, k = {k}")
    print(f"//------Checked-------//")
    output = sol.characterReplacement(s, k)
    output_opt = sol_opt.characterReplacement(s, k)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    s = "AABABBA"; k = 1
    print(f"//------Original-------//")
    print(f"s = {s}, k = {k}")
    print(f"//------Checked-------//")
    output = sol.characterReplacement(s, k)
    output_opt = sol_opt.characterReplacement(s, k)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
