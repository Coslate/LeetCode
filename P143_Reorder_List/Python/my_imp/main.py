#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    head = [1, 2, 3, 4]
    for i in range(len(head)):
        head[i] = ListNode(head[i])

    for i in range(len(head)):
        if i+1 < len(head):
            head[i].next = head[i+1]

    print(f"//------Original-------//")
    print(f"head= {[x.val for x in head]}")
    print(f"//------Checked-------//")
    sol.reorderList(head[0])
    output_list = []
    current_node = head[0]
    while current_node:
        output_list.append(current_node)
        current_node = current_node.next
    print(f"output = {[x.val for x in output_list]}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    head = [1, 2, 3, 4, 5]
    for i in range(len(head)):
        head[i] = ListNode(head[i])

    for i in range(len(head)):
        if i+1 < len(head):
            head[i].next = head[i+1]

    print(f"//------Original-------//")
    print(f"head= {[x.val for x in head]}")
    print(f"//------Checked-------//")
    sol.reorderList(head[0])
    output_list = []
    current_node = head[0]
    while current_node:
        output_list.append(current_node)
        current_node = current_node.next
    print(f"output = {[x.val for x in output_list]}")
    print(f"")
    print(f"")


#---------------Execution---------------#
if __name__ == '__main__':
    main()
