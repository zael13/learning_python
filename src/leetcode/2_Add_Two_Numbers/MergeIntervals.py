from doctest import testmod
from typing import List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ext = 0
        res = ListNode()
        root = res

        while True:
            (val1, l1) = (l1.val, l1.next) if l1 else (0, None)
            (val2, l2) = (l2.val, l2.next) if l2 else (0, None)

            tmp = val1 + val2 + ext
            res.val = tmp % 10
            ext = int(tmp / 10)

            if l1 or l2 or ext:
                res.next = ListNode()
                res = res.next
            else:
                return root

if __name__ == '__main__':
    testmod()
