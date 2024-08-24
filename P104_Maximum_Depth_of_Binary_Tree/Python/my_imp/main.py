#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()

    print(f"//Case1:")
    root = [3,9,20,'null','null',15,7]
    print(f"//------Original-------//")
    print(f"root = {root}")
    print(f"//------Checked-------//")
    map_idx_node = sol.buildTree(root)
    ans = sol.maxDepth(map_idx_node[0])
    print(f"ans = {ans}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    root = [1, 'null', 2]
    print(f"//------Original-------//")
    print(f"root = {root}")
    print(f"//------Checked-------//")
    map_idx_node = sol.buildTree(root)
    ans = sol.maxDepth(map_idx_node[0])
    print(f"ans = {ans}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
