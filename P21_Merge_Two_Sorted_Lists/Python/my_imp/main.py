#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    sol_opt = OptSolution()

    print(f"//Case1:")
    list1 = [ListNode(1), ListNode(2), ListNode(4)]
    list2 = [ListNode(1), ListNode(3), ListNode(4)]
    for index, i in enumerate(list1):
        if index+1 < len(list1):
            i.next = list1[index+1]
    head1 = list1[0]
    for index, i in enumerate(list2):
        if index+1 < len(list2):
            i.next = list2[index+1]
    head2 = list2[0]
    print(f"//------Original-------//")
    print(f"list1 = {[x.val for x in list1]}")
    print(f"list2 = {[x.val for x in list2]}")
    print(f"//------Checked-------//")
    #output = sol.mergeTwoLists(head1, head2)
    output = sol_opt.mergeTwoLists(head1, head2)
    output_list = []
    while output:
        output_list.append(output)
        output = output.next
    print(f"output = {[x.val for x in output_list]}")
    print(f"")
    print(f"")

    print(f"//Case2:")
    list1 = []
    list2 = []
    for index, i in enumerate(list1):
        if index+1 < len(list1):
            i.next = list1[index+1]
    head1 = None
    for index, i in enumerate(list2):
        if index+1 < len(list2):
            i.next = list2[index+1]
    head2 = None
    print(f"//------Original-------//")
    print(f"list1 = {[x.val for x in list1]}")
    print(f"list2 = {[x.val for x in list2]}")
    print(f"//------Checked-------//")
    #output = sol.mergeTwoLists(head1, head2)
    output = sol_opt.mergeTwoLists(head1, head2)
    output_list = []
    while output:
        output_list.append(output)
        output = output.next
    print(f"output = {[x.val for x in output_list]}")
    print(f"")
    print(f"")

    print(f"//Case3:")
    list1 = []
    list2 = [ListNode(0)]
    for index, i in enumerate(list1):
        if index+1 < len(list1):
            i.next = list1[index+1]
    head1 = None
    for index, i in enumerate(list2):
        if index+1 < len(list2):
            i.next = list2[index+1]
    head2 = list2[0]
    print(f"//------Original-------//")
    print(f"list1 = {[x.val for x in list1]}")
    print(f"list2 = {[x.val for x in list2]}")
    print(f"//------Checked-------//")
    #output = sol.mergeTwoLists(head1, head2)
    output = sol_opt.mergeTwoLists(head1, head2)
    output_list = []
    while output:
        output_list.append(output)
        output = output.next
    print(f"output = {[x.val for x in output_list]}")
    print(f"")
    print(f"")




#---------------Execution---------------#
if __name__ == '__main__':
    main()
