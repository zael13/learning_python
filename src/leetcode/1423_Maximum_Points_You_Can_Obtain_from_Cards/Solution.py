from doctest import testmod
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        >>> t = Solution()
        >>> t.maxScore([1,2,3,4,5,6,1], 3)
        12

        >>> t = Solution()
        >>> t.maxScore([2,2,2], 2)
        4

        >>> t = Solution()
        >>> t.maxScore([9,7,7,9,7,7,9], 7)
        55
        """

        max_sum = sum(cardPoints[:k])
        tmp_sum = max_sum

        for i in range(k):
            tmp_sum = tmp_sum + cardPoints[-i-1] - cardPoints[k-i-1]
            max_sum = max(max_sum, tmp_sum)

        return max_sum

if __name__ == '__main__':
    testmod()
