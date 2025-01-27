#! /usr/bin/env python3

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
    head = [1,2,3,4,5]
    left = 2
    right = 4
    head_node = build_list(head)
    new_head = Solution().reverseBetween(head_node, left, right)
    print(f"ans = ", end='')
    print_linked_list(new_head)

    print(f"//Case2:")
    head = [5]
    left = 1
    right = 1
    head_node = build_list(head)
    new_head = Solution().reverseBetween(head_node, left, right)
    print(f"ans = ", end='')
    print_linked_list(new_head)

    print(f"//Case3:")
    head = [3, 5]
    left = 1
    right = 2
    head_node = build_list(head)
    new_head = Solution().reverseBetween(head_node, left, right)
    print(f"ans = ", end='')
    print_linked_list(new_head)


#---------------Execution---------------#
if __name__ == '__main__':
    main()
