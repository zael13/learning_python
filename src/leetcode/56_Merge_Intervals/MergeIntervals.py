from doctest import testmod
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        >>> t = Solution()
        >>> t.merge([[1,3],[2,6],[8,10],[15,18]])
        [[1, 6], [8, 10], [15, 18]]

        >>> t = Solution()
        >>> t.merge([[15,18],[2,6],[8,10],[1,3]])
        [[1, 6], [8, 10], [15, 18]]

        >>> t = Solution()
        >>> t.merge([[1,4],[4,5]])
        [[1, 5]]

        >>> t = Solution()
        >>> t.merge([[1,4],[1,4]])
        [[1, 4]]

        >>> t = Solution()
        >>> t.merge([[1,4],[2,3]])
        [[1, 4]]
        """
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                if res[-1][1] <= intervals[i][1]:
                    res[-1][1] = intervals[i][1]
            else:
                res.append(intervals[i])
        return res


if __name__ == '__main__':
    testmod()
