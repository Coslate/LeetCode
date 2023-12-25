#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()
    nums = [1, 0, 1, 0, 1]
    goal = 2
    print(f"//Case1:")
    print(f"//------Original-------//")
    print(f"nums = {nums}")
    print(f"goal = {goal}")
    print(f"//------Checked-------//")
    output = sol.numSubarraysWithSum(nums, goal)
    print(f"output = {output}")
    print(f"")
    print(f"")

    nums = [0, 0, 0, 0, 0]
    goal = 0
    print(f"//Case2:")
    print(f"//------Original-------//")
    print(f"nums = {nums}")
    print(f"goal = {goal}")
    print(f"//------Checked-------//")
    output = sol.numSubarraysWithSum(nums, goal)
    print(f"output = {output}")
    print(f"")
    print(f"")

    nums = [0, 1, 1, 1, 1]
    goal = 3
    print(f"//Case3:")
    print(f"//------Original-------//")
    print(f"nums = {nums}")
    print(f"goal = {goal}")
    print(f"//------Checked-------//")
    output = sol.numSubarraysWithSum(nums, goal)
    print(f"output = {output}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
