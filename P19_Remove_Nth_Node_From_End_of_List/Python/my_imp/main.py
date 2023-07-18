#! /usr/bin/env python3

from solution import *

def main():
    sol = Solution()
    llist_obj = LinkedList()
    llist_obj.insertBackNode(1)
    llist_obj.insertBackNode(2)
    llist_obj.insertBackNode(3)
    llist_obj.insertBackNode(4)
    llist_obj.insertBackNode(5)

    print(f"nums = {llist_obj.printLinkedList()}")

    llist_obj.head = sol.removeNthFromEnd(llist_obj.head, 2)
    print(f"ans = {llist_obj.printLinkedList()}")

#---------------Execution---------------#
if __name__ == '__main__':
    main()
