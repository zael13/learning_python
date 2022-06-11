from doctest import testmod


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """
        >>> t = Solution()
        >>> t.bitwiseComplement(0)
        1

        >>> t = Solution()
        >>> t.bitwiseComplement(1)
        0

        >>> t = Solution()
        >>> t.bitwiseComplement(5)
        2

        >>> t = Solution()
        >>> t.bitwiseComplement(7)
        0
        """
        mask, tmp = 0, n

        if not n:
            return 1

        while tmp:
            mask = (mask << 1) | 1
            tmp >>= 1

        return mask ^ n


if __name__ == '__main__':
    testmod()
