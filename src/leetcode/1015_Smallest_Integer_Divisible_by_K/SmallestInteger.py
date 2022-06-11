from doctest import testmod
from typing import List


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """
        >>> t = Solution()
        >>> t.smallestRepunitDivByK(1)
        1

        >>> t = Solution()
        >>> t.smallestRepunitDivByK(111)
        3

        >>> t = Solution()
        >>> t.smallestRepunitDivByK(2)
        -1

        >>> t = Solution()
        >>> t.smallestRepunitDivByK(81111)
        -1
        """
        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder, res = 1, 1
        seen_remainders = set()

        while True:
            remainder = res % k

            if remainder == 0:
                return len(str(res))
            else:
                res = res * 10 + 1

            if remainder in seen_remainders:
                return -1
            else:
                seen_remainders.add(remainder)


        # while remainder % k != 0:
        #     remainder = (remainder * 10 + 1) % k
        #
        #     if remainder in seen_remainders:
        #         return -1
        #     else:
        #         seen_remainders.add(remainder)
        #
        # return len(str(remainder))

if __name__ == '__main__':
    testmod()
