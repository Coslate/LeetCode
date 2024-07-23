#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    head_list = [ListNode(3), ListNode(2), ListNode(0), ListNode(4)]
    for index, i in enumerate(head_list):
        if index+1 < len(head_list):
            i.next = head_list[index+1]
    head_list[-1].next = head_list[1]
    head = head_list[0]
    print(f"//------Original-------//")
    print(f"head_list = {[x.val for x in head_list]}")
    print(f"head = {head}")
    print(f"//------Checked-------//")
    output = sol.hasCycle(head)
    output_opt = sol_opt.hasCycle(head)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    head_list = [ListNode(1), ListNode(2)]
    for index, i in enumerate(head_list):
        if index+1 < len(head_list):
            i.next = head_list[index+1]
    head_list[-1].next = head_list[0]
    head = head_list[0]
    print(f"//------Original-------//")
    print(f"head_list = {[x.val for x in head_list]}")
    print(f"head = {head}")
    print(f"//------Checked-------//")
    output = sol.hasCycle(head)
    output_opt = sol_opt.hasCycle(head)
    print(f"output = {output}")
    print(f"output_opt = {output_opt}")
    print(f"")
    print(f"")



#---------------Execution---------------#
if __name__ == '__main__':
    main()
