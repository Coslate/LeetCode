#! /usr/bin/env python3

from collections import deque
from solution import *

def build_list(head: List[int]) -> Optional[TreeNode]:
    head_list = [TreeNode(_) for _ in head]
    for index, i in enumerate(head_list):
        if index+1 < len(head_list):
            i.next = head_list[index+1]
        else:
            i.next = None
    return head_list[0]

def print_tree(head: Optional[TreeNode]) -> None:
    cur = head
    print(f"[", end='')
    queue = deque([cur])
    while queue:
        top = queue.popleft()
        if top is not None:
            print(f"{top.val} ", end='')
        else:
            print(f"null ", end='')
            continue

        if top.left is not None:
            queue.append(top.left)
        else:
            queue.append(None)

        if top.right is not None:
            queue.append(top.right)
        else:
            queue.append(None)
    print(f"]")



def main():
    print(f"//Case1:")
    root = [1, 2, 3, 4, 5]
    root_node_list = [TreeNode(_, None, None) for _ in root]
    root_node_list[0].left = root_node_list[1]
    root_node_list[0].right = root_node_list[2]
    root_node_list[1].left = root_node_list[3]
    root_node_list[1].right = root_node_list[4]
    print(f"original tree = ")
    print_tree(root_node_list[0])
    new_head = Solution().upsideDownBinaryTree(root_node_list[0])
    print(f"ans = ")
    print_tree(new_head)

    print(f"//Case2:")
    root = []
    print(f"original tree = ")
    print_tree(None)
    new_head = Solution().upsideDownBinaryTree(None)
    print(f"ans = ")
    print_tree(new_head)

    print(f"//Case3:")
    root = [1]
    root_node_list = [TreeNode(_, None, None) for _ in root]
    print(f"original tree = ")
    print_tree(root_node_list[0])
    new_head = Solution().upsideDownBinaryTree(root_node_list[0])
    print(f"ans = ")
    print_tree(new_head)



#---------------Execution---------------#
if __name__ == '__main__':
    main()
