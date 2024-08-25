#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()

    print(f"//Case1:")
    root = [4,2,7,1,3,6,9]
    print(f"//------Original-------//")
    print(f"root = {root}")
    print(f"//------Checked-------//")
    map_idx_node = sol.buildTree(root)
    sol.printTree(map_idx_node[0])
    new_root = sol.invertTree(map_idx_node[0])
    print(f"ans = ")
    sol.printTree(new_root)
    print(f"")
    print(f"")

    print(f"//Case2:")
    root = [2, 1, 3]
    print(f"//------Original-------//")
    print(f"root = {root}")
    print(f"//------Checked-------//")
    map_idx_node = sol.buildTree(root)
    sol.printTree(map_idx_node[0])
    new_root = sol.invertTree(map_idx_node[0])
    print(f"ans = ")
    sol.printTree(new_root)
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
