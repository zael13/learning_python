# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        p2 = self.split(head)
        self.merge(head, p2)

    @staticmethod
    def split(head):
        tmp = head
        p1 = head
        p2 = head

        while p2:
            p2 = p2.next
            if p2:
                p2 = p2.next
            tmp = p1
            p1 = p1.next
        tmp.next = None

        prev_p = None
        next_p = p1.next
        while p1 and p1.next:
            next_p = p1.next
            p1.next = prev_p
            prev_p = p1
            p1 = next_p
        p1.next = prev_p

        return p1

    @staticmethod
    def merge(a, b):
        while a:
            next_a = a.next
            if b:
                next_b = b.next
            else:
                a.next = b
                break

            a.next = b
            b.next = next_a
            a = next_a
            b = next_b
