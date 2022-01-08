import collections
from doctest import testmod
from typing import List
from collections import Counter

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        >>> t = Solution()
        >>> t.findJudge(3,[[1,3],[2,3]])
        3

        >>> t = Solution()
        >>> t.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])
        3

        >>> t = Solution()
        >>> t.findJudge(1, [])
        1

        >>> t = Solution()
        >>> t.findJudge(3, [[1,3],[2,3],[3,1]])
        -1
        """
        if n == 1 and len(trust) == 0:
            return 1

        j = set(i for i in range(1, n+1))
        b = collections.defaultdict(int)

        for i in trust:
            if i[0] in j:
                j.remove(i[0])
            b[i[1]] += 1

        if len(j) == 1:
            res = j.pop()
            return res if b[res] == n-1 else -1
        else:
            return -1


if __name__ == '__main__':
    testmod()
