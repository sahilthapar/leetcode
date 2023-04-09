# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(next=head)
    prev = dummy
    cur = head
    while cur:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    return dummy.next
