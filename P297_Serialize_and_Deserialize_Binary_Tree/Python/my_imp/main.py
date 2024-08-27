#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    root = [1,2,3,'null','null',4,5]
    print(f"//------Original-------//")
    print(f"root = {root}")
    print(f"//------Checked-------//")
    map_idx_node = sol.buildTree(root)
    tree_list = sol.treeNode2List(map_idx_node[0])
    print(f"tree_list = {tree_list}")
    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(map_idx_node[0]))
    sol.printTree(map_idx_node[0])
    print(f"XXXXXXXXXXXXXXXXX")
    sol.printTree(ans)
    tree_list_ans = sol.treeNode2List(ans)
    print(f"tree_list_ans = {tree_list_ans}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    root = []
    print(f"//------Original-------//")
    print(f"root = {root}")
    print(f"//------Checked-------//")
    map_idx_node = sol.buildTree(root)
    if map_idx_node: 
        tree_list = sol.treeNode2List(map_idx_node[0])
    else:
        tree_list = []

    print(f"tree_list = {tree_list}")
    ser = Codec()
    deser = Codec()
    if map_idx_node:
        ans = deser.deserialize(ser.serialize(map_idx_node[0]))
        sol.printTree(map_idx_node[0])
    else:
        ans = deser.deserialize(ser.serialize(None))
        sol.printTree(None)

    print(f"XXXXXXXXXXXXXXXXX")
    sol.printTree(ans)
    tree_list_ans = sol.treeNode2List(ans)
    print(f"tree_list_ans = {tree_list_ans}")
    print(f"")
    print(f"")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
