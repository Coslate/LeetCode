#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    nums = [3, 2, 2, 3]
    val  = 3
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"nums = {nums}, val = {val}")

    print(f"//------Removed-------//")
    #k = sol.removeElement(nums, val)
    k = sol_opt.removeElement(nums, val)
    print(f"nums = {nums}")
    print(f"k = {k}")

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val  = 2
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"nums = {nums}, val = {val}")

    print(f"//------Removed-------//")
    #k = sol.removeElement(nums, val)
    k = sol_opt.removeElement(nums, val)
    print(f"nums = {nums}")
    print(f"k = {k}")





#---------------Execution---------------#
if __name__ == '__main__':
    main()
