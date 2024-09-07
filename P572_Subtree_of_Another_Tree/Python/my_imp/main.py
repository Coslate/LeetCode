#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    root = [3, 4, 5, 1, 2]
    subRoot = [4, 1, 2]
    print(f"//------Original-------//")
    map_idx_node_rootTree = sol.buildTree(root)
    map_idx_node_subTree = sol.buildTree(subRoot)
    tree_list_root = sol.treeNode2List(map_idx_node_rootTree[0])
    tree_list_sub = sol.treeNode2List(map_idx_node_subTree[0])
    print(f"root = {root}")
    print(f"subRoot = {subRoot}")
    print(f"tree_list_sub = {tree_list_sub}")
    print(f"tree_list_root = {tree_list_root}")
    print(f"//------Checked-------//")
    ans = sol.isSubtree(map_idx_node_rootTree[0], map_idx_node_subTree[0])
    print(f"ans = {ans}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    root = [3,4,5,1,2,"null","null","null","null",0]
    subRoot = [4, 1, 2]
    print(f"//------Original-------//")
    map_idx_node_rootTree = sol.buildTree(root)
    map_idx_node_subTree = sol.buildTree(subRoot)
    tree_list_root = sol.treeNode2List(map_idx_node_rootTree[0])
    tree_list_sub = sol.treeNode2List(map_idx_node_subTree[0])
    print(f"root = {root}")
    print(f"subRoot = {subRoot}")
    print(f"tree_list_sub = {tree_list_sub}")
    print(f"tree_list_root = {tree_list_root}")
    print(f"//------Checked-------//")
    ans = sol.isSubtree(map_idx_node_rootTree[0], map_idx_node_subTree[0])
    print(f"ans = {ans}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
