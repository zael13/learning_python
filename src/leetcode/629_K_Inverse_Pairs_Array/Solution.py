from doctest import testmod
from typing import List


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        """
        >>> t = Solution()
        >>> t.kInversePairs(3, 0)
        1

        >>> t = Solution()
        >>> t.kInversePairs(3, 1)
        2

        >>> t = Solution()
        >>> t.kInversePairs(4, 4)
        5

        >>> t = Solution()
        >>> t.kInversePairs(1000, 50)
        2219012
        """

        dp0 = [0] * (k+1)
        M = 10**9 + 7

        for i in range(1, n+1):
            dp1 = [0] * len(dp0)
            for j in range(len(dp0)):
                if j == 0:
                    dp1[j] = 1
                    tmp_sum = dp0[j]
                else:
                    tmp_sum += dp0[j] - dp0[j-i] if j-i >= 0 else dp0[j]
                    dp1[j] = tmp_sum % M
            dp0 = dp1
        return dp0[-1] if k else 1

if __name__ == '__main__':
    testmod()
