import itertools
from collections import defaultdict


class Solution:
    def solution(self, l):
        """
        >>> t = Solution()
        >>> t.solution([1, 2, 3, 4, 5, 6])
        3

       >>> t = Solution()
        >>> t.solution([1, 2, 3, 4, 5, 8, 10])
        6

       >>> t = Solution()
        >>> t.solution([1, 2, 3, 4, 4, 3, 2, 1])
        6

        >>> t = Solution()
        >>> t.solution([1, 1 ,1])
        1

        >>> t = Solution()
        >>> t.solution([5, 7 ,11, 23, 111])
        0

        >>> t = Solution()
        >>> t.solution([1, 1])
        0

        >>> t = Solution()
        >>> t.solution([5,4,3,2,1])
        0

        >>> t = Solution()
        >>> t.solution([1, 1 ,1, 1])
        4

        """
        comb = itertools.combinations(l, 3)

        res = 0
        for i in comb:
            if i[2] % i[1] == 0 and i[1] % i[0] == 0:
                res += 1
        return res


if __name__ == '__main__':
    testmod()