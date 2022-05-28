from doctest import testmod
from typing import List
from functools import lru_cache


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        >>> t = Solution()
        >>> t.cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]])
        24

        >>> t = Solution()
        >>> t.cherryPickup([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]])
        28

        >>> t = Solution()
        >>> t.cherryPickup([[8,8,10,9,1,7],[8,8,1,8,4,7],[8,6,10,3,7,7],[3,0,9,3,2,7],[6,8,9,4,2,5],[1,1,5,8,8,1],[5,6,5,2,9,9],[4,4,6,2,5,4],[4,4,5,3,1,6],[9,2,2,1,9,3]])
        146
        """

        @lru_cache(None)
        def nextStep(x_r1, x_r2, y):
            res = 0

            if x_r1 < 0 or x_r1 >= len(grid[0]) or  x_r2 < 0 or x_r2 >= len(grid[0]):
                return -1

            res += grid[y][x_r1]
            if x_r1 != x_r2:
                res += grid[y][x_r2]

            if y != len(grid) - 1:
                res += max(nextStep(x1, x2, y + 1)
                    for x1 in [x_r1, x_r1 + 1, x_r1 - 1]
                    for x2 in [x_r2, x_r2 + 1, x_r2 - 1])
            return res

        return nextStep(0, len(grid[0]) - 1, 0)


if __name__ == '__main__':
    testmod()
