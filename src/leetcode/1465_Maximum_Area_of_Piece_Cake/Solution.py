from doctest import testmod
from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        """
        >>> t = Solution()
        >>> t.maxArea(5, 4, [1,2,4], [1,3])
        4
 
        >>> t = Solution()
        >>> t.maxArea(5, 4, [3,1], [1])
        6

        >>> t = Solution()
        >>> t.maxArea(1000000000, 1000000000, [2], [2])
        81
        """

        horizontalCuts.sort()
        verticalCuts.sort()

        max_h = max(horizontalCuts[0], h - horizontalCuts[-1])
        max_w = max(verticalCuts[0], w - verticalCuts[-1])

        for i in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[i] - horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)):
            max_w = max(max_w, verticalCuts[i] - verticalCuts[i-1])

        return (max_w * max_h) % (10**9 + 7)

if __name__ == '__main__':
    testmod()
