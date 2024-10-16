#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    root = [6,2,8,0,4,7,9,None,None,3,5]
    p = TreeNode(2)
    q = TreeNode(8)
    print(f"//------Original-------//")
    print(f"root = {root}")
    tree_test = sol.buildTreeTest(root)
    tree_list_root = sol.treeNode2List(tree_test[0])
    print(f"tree_list_root = {tree_list_root}")
    print(f"//------Checked-------//")
    ans = sol.lowestCommonAncestor(tree_test[0], p, q)
    print(f"ans = {ans.val}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    root = [6,2,8,0,4,7,9,None,None,3,5]
    p = TreeNode(2)
    q = TreeNode(4)
    print(f"//------Original-------//")
    print(f"root = {root}")
    tree_test = sol.buildTreeTest(root)
    tree_list_root = sol.treeNode2List(tree_test[0])
    print(f"tree_list_root = {tree_list_root}")
    print(f"//------Checked-------//")
    ans = sol.lowestCommonAncestor(tree_test[0], p, q)
    print(f"ans = {ans.val}")
    print(f"")
    print(f"")

    print(f"//Case3:")
    root = [2,1]
    p = TreeNode(2)
    q = TreeNode(1)
    print(f"//------Original-------//")
    print(f"root = {root}")
    tree_test = sol.buildTreeTest(root)
    tree_list_root = sol.treeNode2List(tree_test[0])
    print(f"tree_list_root = {tree_list_root}")
    print(f"//------Checked-------//")
    ans = sol.lowestCommonAncestor(tree_test[0], p, q)
    print(f"ans = {ans.val}")
    print(f"")
    print(f"")



#---------------Execution---------------#
if __name__ == '__main__':
    main()
