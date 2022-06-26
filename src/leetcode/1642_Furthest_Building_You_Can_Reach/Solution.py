from doctest import testmod
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        >>> t = Solution()
        >>> t.furthestBuilding([4,2,7,6,9,14,12],5,1)
        4

        >>> t = Solution()
        >>> t.furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2)
        7

        >>> t = Solution()
        >>> t.furthestBuilding([14,3,19,3], 17,0)
        3
        """
        largest = []
        cnt = 0
        min_idx = None
        for i in range(1, len(heights)):
            delta = heights[i] - heights[i - 1]
            if delta > 0:
                if len(largest) < ladders:
                    largest.append(delta)
                    if len(len(largest) == ladders):

                        largest.sort(reverse=True)
                else:
                    if largest and delta > largest[-1]:
                        cnt += largest[-1]
                        largest[-1] = delta
                        largest.sort(reverse=True)
                    else:
                        cnt += delta

                if cnt > bricks:
                    return i-1
        return len(heights)-1





if __name__ == '__main__':
    testmod()
