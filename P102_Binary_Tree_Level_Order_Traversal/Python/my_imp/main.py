#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    root = [3,9,20,'null','null',15,7]
    print(f"//------Original-------//")
    print(f"root = {root}")
    print(f"//------Checked-------//")
    map_idx_node = sol.buildTree(root)
    sol.printTree(map_idx_node[0])
    ans = sol.levelOrder(map_idx_node[0])
    ans_opt = sol_opt.levelOrder(map_idx_node[0])
    print(f"ans = {ans}")
    print(f"ans_opt = {ans_opt}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    root = [1]
    print(f"//------Original-------//")
    print(f"root = {root}")
    print(f"//------Checked-------//")
    map_idx_node = sol.buildTree(root)
    sol.printTree(map_idx_node[0])
    ans = sol.levelOrder(map_idx_node[0])
    ans_opt = sol_opt.levelOrder(map_idx_node[0])
    print(f"ans = {ans}")
    print(f"ans_opt = {ans_opt}")
    print(f"")
    print(f"")

    print(f"//Case3:")
    root = []
    print(f"//------Original-------//")
    print(f"root = {root}")
    print(f"//------Checked-------//")
    if root: 
        map_idx_node = sol.buildTree(root)
    else:
        map_idx_node[0] = None

    sol.printTree(map_idx_node[0])
    ans = sol.levelOrder(map_idx_node[0])
    ans_opt = sol_opt.levelOrder(map_idx_node[0])
    print(f"ans = {ans}")
    print(f"ans_opt = {ans_opt}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
