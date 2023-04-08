# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    while head and head.val == val:
        head = head.next
    if not head:
        return None
    prev = head
    cur = head.next
    while cur:
        if cur.val == val:
            prev.next = cur.next
            cur = cur.next
        else:
            prev = cur
            cur = cur.next
    return head
