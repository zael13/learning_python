from doctest import testmod
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        """
        >>> t = Solution()
        >>> t.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]])
        [1, -1, -1, -1, -1]

        >>> t = Solution()
        >>> t.findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]])
        [0, 1, 2, 3, 4, -1]

        >>> t = Solution()
        >>> t.findBall([[-1]])
        [-1]

        >>> t = Solution()
        >>> t.findBall([[-1]])
        [-1]

        """

        for y in range(len(grid)-1, -1, -1):
        #     for x in range(len(grid[0])):
        #         if x == 0:
        #             if grid[y][x] == -1:
        #                 grid[y][x] = None
        #             else:
        #                 grid[y][x] =1
        #         if grid[y][x] is None:
        #             pass
        #         elif x == len(grid[0])-1:
        #             if grid[y][x] == 1:
        #                 grid[y][x] = None
        #             else:
        #                 grid[y][x] = x-1
        #         else:
        #             if grid[y][x] == 1 and grid[y][x+1] == -1:
        #                 grid[y][x] = None
        #                 grid[y][x+1] = None
        #             else:
        #                 if grid[y][x] == 1:
        #                     grid[y][x] = x + 1
        #                 else:
        #                     grid[y][x] = x - 1
        #
        #     for x in range(len(grid[0])):
        #         if y and grid[y][x] is None:
        #             if x == 0:
        #                 if grid[y-1][x+1] == -1:
        #                     grid[y - 1][x + 1] = None
        #                 grid[y - 1][x + 1]
        #             elif x == len(grid[0])-1:
        #                 if grid[y-1][x-1] == 1:
        #                     grid[y - 1][x - 1] = None
        #             else:
        #                 if grid[y-1][x+1] == -1:
        #                     grid[y - 1][x + 1] = None
        #                 if grid[y-1][x-1] == 1:
        #                     grid[y - 1][x - 1] = None


            for x in range(len(grid[0])):
                if y == len(grid) - 1:
                    if grid[y][x] is None:
                        pass
                    elif x == 0:
                        if grid[y][x] == -1:
                            grid[y][x] = None
                        elif grid[y][x] == 1 and grid[y][x+1] == -1:
                            grid[y][x] = None
                            grid[y][x+1] = None
                        else:
                            grid[y][x] = grid[y+1][x+1]
                    elif x == len(grid[0])-1:
                        if grid[y][x] == 1:
                            grid[y][x] = None
                        else:
                            grid[y][x] = x-1
                    else:
                        if grid[y][x] == 1 and grid[y][x+1] == -1:
                            grid[y][x] = None
                            grid[y][x+1] = None
                        else:
                            if grid[y][x] == 1:
                                grid[y][x] = x + 1
                            else:
                                grid[y][x] = x - 1
                else:
                    if grid[y][x] is None:
                        pass
                    elif x == 0:
                        if grid[y][x] == -1:
                            grid[y][x] = None
                        elif grid[y][x] == 1 and grid[y][x+1] == -1:
                            grid[y][x] = None
                            grid[y][x+1] = None
                        else:
                            grid[y][x] = grid[y+1][x+1]
                    elif x == len(grid[0])-1:
                        if grid[y][x] == 1:
                            grid[y][x] = None
                        else:
                            grid[y][x] = grid[y+1][x-1]
                    else:
                        if grid[y][x] == 1 and grid[y][x+1] == -1:
                            grid[y][x] = None
                            grid[y][x+1] = None
                        else:
                            if grid[y][x] == 1:
                                grid[y][x] = grid[y+1][x+1]
                            else:
                                grid[y][x] = grid[y+1][x-1]

        # print(grid)
        return [i if i is not None else -1 for i in grid[0]]

if __name__ == '__main__':
    testmod()
