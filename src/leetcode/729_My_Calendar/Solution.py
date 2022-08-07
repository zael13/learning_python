from doctest import testmod
from typing import List
import bisect

class Solution:
    def __init__(self):
        self.data = [(0, 0), (10**9, 10**9)]

    def book(self, start: int, end: int) -> bool:
        """
        >>> t = Solution()
        >>> t.book(2, 3)
        True
        >>> t.book(4, 5)
        True
        >>> t.book(1, 2)
        True

        >>> t = Solution()
        >>> t.book(0, 20)
        True
        >>> t.book(15, 25)
        False
        >>> t.book(20, 10**9)
        True
        """

        # bisect.bisect_left(self.data, (start, end))
        idx = bisect.bisect_left(self.data, (start, end))
        if self.data[idx-1][1] <= start and self.data[idx][0] >= end:
            bisect.insort_left(self.data, (start, end))
            return True
        else:
            return False

if __name__ == '__main__':
    testmod()
