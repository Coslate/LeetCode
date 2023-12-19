#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"nums = {nums}")
    print(f"k = {k}")
    print(f"//------Checked-------//")
    #output = sol.longestOnes(nums, k)
    output = sol_opt.longestOnes(nums, k)
    print(f"output = {output}")
    print(f"")
    print(f"")


    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"nums = {nums}")
    print(f"k = {k}")
    print(f"//------Checked-------//")
    #output = sol.longestOnes(nums, k)
    output = sol_opt.longestOnes(nums, k)
    print(f"output = {output}")
    print(f"")
    print(f"")

    nums = [0, 0, 0, 1]
    k = 4
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"nums = {nums}")
    print(f"k = {k}")
    print(f"//------Checked-------//")
    #output = sol.longestOnes(nums, k)
    output = sol_opt.longestOnes(nums, k)
    print(f"output = {output}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
