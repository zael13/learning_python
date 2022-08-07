from collections import deque
from doctest import testmod
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        """
        >>> t = Solution()
        >>> t.maxResult([1,-1,-2,4,-7,3], 2)
        7

        >>> t = Solution()
        >>> t.maxResult([10,-5,-2,4,0,3], 3)
        17

        >>> t = Solution()
        >>> t.maxResult([1,-5,-20,4,-1,3,-6,-3], 2)
        0

        >>> t = Solution()
        >>> t.maxResult([1], 2)
        1

        >>> t = Solution()
        >>> t.maxResult([-1, -1, -1], 2)
        -2

        >>> t = Solution()
        >>> t.maxResult([40,30,-100,-100,-10,-7,-3,-3], 2)
        -40
        """

        dp = deque([(nums[0], 0)])
        for i in range(1, len(nums)):
            while dp and dp[0][1] + k < i:
                dp.popleft()
            cost = nums[i] + dp[0][0]
            while dp and cost >= dp[-1][0]:
                dp.pop()
            dp.append((cost, i))
        return dp[-1][0]


if __name__ == '__main__':
    testmod()
