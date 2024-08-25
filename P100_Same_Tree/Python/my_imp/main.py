#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()

    print(f"//Case1:")
    p = [1, 2, 3]
    q = [1, 2, 3]
    print(f"//------Original-------//")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"//------Checked-------//")
    map_idx_node1 = sol.buildTree(p)
    map_idx_node2 = sol.buildTree(q)
    ans = sol.isSameTree(map_idx_node1[0], map_idx_node2[0])
    print(f"ans = {ans}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    p = [1, 2]
    q = [1, 'null', 2]
    print(f"//------Original-------//")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"//------Checked-------//")
    map_idx_node1 = sol.buildTree(p)
    map_idx_node2 = sol.buildTree(q)
    ans = sol.isSameTree(map_idx_node1[0], map_idx_node2[0])
    print(f"ans = {ans}")
    print(f"")
    print(f"")

    print(f"//Case3:")
    p = [1, 2, 1]
    q = [1, 1, 2]
    print(f"//------Original-------//")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"//------Checked-------//")
    map_idx_node1 = sol.buildTree(p)
    map_idx_node2 = sol.buildTree(q)
    ans = sol.isSameTree(map_idx_node1[0], map_idx_node2[0])
    print(f"ans = {ans}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
