#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    head_list = [ListNode(i) for i in range(1, 6)]
    for index, i in enumerate(head_list):
        if index+1 < len(head_list):
            i.next = head_list[index+1]
    head = head_list[0]
    print(f"//------Original-------//")
    print(f"head_list = {[x.val for x in head_list]}")
    print(f"head = {head}")
    print(f"//------Checked-------//")
    output = sol.reverseList(head)
    cur = []
    while(output is not None):
        cur.append(output)
        output = output.next
    print(f"output_list = {[x.val for x in cur]}")
    print(f"output = {output}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    head_list = [ListNode(i) for i in range(1, 3)]
    for index, i in enumerate(head_list):
        if index+1 < len(head_list):
            i.next = head_list[index+1]
    head = head_list[0]
    print(f"//------Original-------//")
    print(f"head_list = {[x.val for x in head_list]}")
    print(f"head = {head}")
    print(f"//------Checked-------//")
    output = sol.reverseList(head)
    cur = []
    while(output is not None):
        cur.append(output)
        output = output.next
    print(f"output_list = {[x.val for x in cur]}")
    print(f"output = {output}")
    print(f"")
    print(f"")



#---------------Execution---------------#
if __name__ == '__main__':
    main()
