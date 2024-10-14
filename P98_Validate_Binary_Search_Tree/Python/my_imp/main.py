#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    root = [2,1,3]
    print(f"//------Original-------//")
    print(f"root = {root}")
    tree_test = sol.buildTreeTest(root)
    tree_list_root = sol.treeNode2List(tree_test[0])
    print(f"tree_list_root = {tree_list_root}")
    print(f"//------Checked-------//")
    ans = sol.isValidBST(tree_test[0])
    ans_opt = sol_opt.isValidBST(tree_test[0])
    print(f"ans = {ans}")
    print(f"ans_opt = {ans_opt}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    root = [5,1,4,None,None,3,6]
    print(f"//------Original-------//")
    print(f"root = {root}")
    tree_test = sol.buildTreeTest(root)
    tree_list_root = sol.treeNode2List(tree_test[0])
    print(f"tree_list_root = {tree_list_root}")
    print(f"//------Checked-------//")
    ans = sol.isValidBST(tree_test[0])
    ans_opt = sol_opt.isValidBST(tree_test[0])
    print(f"ans = {ans}")
    print(f"ans_opt = {ans_opt}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
