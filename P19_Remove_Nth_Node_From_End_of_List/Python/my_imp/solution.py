from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBackNode(self, val: int) -> None:
        if self.head is None:
            self.head = ListNode(val, next=None)
        else:
            cur_head = self.head
            while(cur_head.next is not None):
                cur_head = cur_head.next
            cur_head.next = ListNode(val, next=None)

    def printLinkedList(self) -> str:
        cur_head = self.head
        ret_str = f"["
        while(cur_head is not None):
            if cur_head.next is None:
                ret_str += f"{cur_head.val}"
            else:
                ret_str += f"{cur_head.val}, "
            cur_head = cur_head.next
        ret_str += f"]"
        return ret_str

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # LinkedList Traversing | Time: O(n) | Space: O(1)
        if head is None:
            return None

        cur_head = head
        length = 0
        cnt = 0

        while cur_head is not None:
            length += 1
            cur_head = cur_head.next

        cur_head = head
        prev_head = head
        del_node_pos = length - n

        while cnt < del_node_pos:
            prev_head = cur_head
            cur_head = cur_head.next
            cnt += 1

        if del_node_pos == 0:
            head = cur_head.next
            cur_head.next = None
        else:
            prev_head.next = cur_head.next
            cur_head.next = None

        return head
