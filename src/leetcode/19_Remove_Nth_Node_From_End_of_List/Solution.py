from doctest import testmod
from typing import List


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        >>> t = Solution()
        >>> t.solve([[3,1,1],[2,5,1],[1,5,5],[2,1,1]])
        24
        """

        node = head
        l = 0
        while node:
            node = node.next
            l += 1

        node = head
        prev = None
        idx = 0
        while node:
            if idx == l-n:
                prev.next = node.next
                return head
            prev = node
            node = node.next
            idx += 1

        return None

if __name__ == '__main__':
    testmod()
