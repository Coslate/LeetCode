#! /usr/bin/env python3

from collections import deque
from solution import *

def build_list(head: List[int]) -> Optional[ListNode]:
    head_list = [ListNode(_) for _ in head]
    for index, i in enumerate(head_list):
        if index+1 < len(head_list):
            i.next = head_list[index+1]
        else:
            i.next = None
    return head_list[0]

def print_linked_list(head: Optional[ListNode]) -> None:
    cur = head
    print(f"[", end='')
    while cur:
        if cur.next == None:
            print(f"{cur.val}]")
        else:
            print(f"{cur.val} ", end='')

        cur = cur.next

def main():
    print(f"//Case1:")
    head = [1, 2, 2, 1]
    head_node = build_list(head)
    print(f'ans = {Solution().isPalindrome(head_node)}')

    print(f"//Case2:")
    head = [1, 2]
    head_node = build_list(head)
    print(f'ans = {Solution().isPalindrome(head_node)}')

#---------------Execution---------------#
if __name__ == '__main__':
    main()
