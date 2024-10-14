#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    print(f"//------Original-------//")
    print(f"preorder = {preorder}")
    print(f"inorder = {inorder}")
    print(f"//------Checked-------//")
    ans_root_node = sol.buildTree(preorder, inorder)
    tree_list_root = sol.treeNode2List(ans_root_node)
    print(f"ans, tree_list_root = {tree_list_root}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    preorder = [-1]
    inorder = [-1]
    print(f"//------Original-------//")
    print(f"preorder = {preorder}")
    print(f"inorder = {inorder}")
    print(f"//------Checked-------//")
    ans_root_node = sol.buildTree(preorder, inorder)
    tree_list_root = sol.treeNode2List(ans_root_node)
    print(f"ans, tree_list_root = {tree_list_root}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
