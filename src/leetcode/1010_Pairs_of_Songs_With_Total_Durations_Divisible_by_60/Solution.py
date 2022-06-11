from doctest import testmod
from typing import List
from collections import Counter

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        >>> t = Solution()
        >>> t.numPairsDivisibleBy60([30,20,150,100,40])
        3

        >>> t = Solution()
        >>> t.numPairsDivisibleBy60([60,60,60])
        3
        """

        reminders = Counter()
        res = 0

        for i in time:
            r = i % 60
            res += reminders[60-r] if r else reminders[0]
            reminders[r] += 1
        return res

if __name__ == '__main__':
    testmod()
