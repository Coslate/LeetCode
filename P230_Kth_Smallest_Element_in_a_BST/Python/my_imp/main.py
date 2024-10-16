#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    root = [3,1,4,None,2]
    k = 1
    print(f"//------Original-------//")
    print(f"root = {root}")
    tree_test = sol.buildTreeTest(root)
    tree_list_root = sol.treeNode2List(tree_test[0])
    print(f"tree_list_root = {tree_list_root}")
    print(f"//------Checked-------//")
    ans = sol.kthSmallest(tree_test[0], k)
    print(f"ans = {ans}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    root = [5,3,6,2,4,None,None,1]
    k = 3
    print(f"//------Original-------//")
    print(f"root = {root}")
    tree_test = sol.buildTreeTest(root)
    tree_list_root = sol.treeNode2List(tree_test[0])
    print(f"tree_list_root = {tree_list_root}")
    print(f"//------Checked-------//")
    ans = sol.kthSmallest(tree_test[0], k)
    print(f"ans = {ans}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
