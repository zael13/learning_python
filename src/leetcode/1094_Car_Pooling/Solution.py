import collections
from doctest import testmod
from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        >>> t = Solution()
        >>> t.carPooling([[2,1,5],[3,3,7]], 4)
        False

        >>> t = Solution()
        >>> t.carPooling([[2,1,5],[3,3,7]], 5)
        True
        """
        stops = collections.defaultdict(int)

        for i in trips:
            stops[i[1]] += i[0]
            stops[i[2]] -= i[0]

        passagers = 0
        for stop in sorted(stops.keys()):
            passagers += stops[stop]
            if passagers > capacity:
                return False
        return True


if __name__ == '__main__':
    testmod()
