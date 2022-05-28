from doctest import testmod
from typing import List


class Solution:
    def find(self, s: str) -> int:
        """
        >>> t = Solution()
        >>> t.find("aaa")
        3

        >>> t = Solution()
        >>> t.find("a")
        1

        >>> t = Solution()
        >>> t.find("abcabcabcabc")
        4

        >>> t = Solution()
        >>> t.find("abccbaabccba")
        2

        >>> t = Solution()
        >>> t.find("abcabcabcabc")
        4

        >>> t = Solution()
        >>> t.find("abccbaabccba")
        2

        >>> t = Solution()
        >>> t.find("abcabc")
        2

        >>> t = Solution()
        >>> t.find("abcabca")
        1

        >>> t = Solution()
        >>> t.find("abcabcd")
        1

        >>> t = Solution()
        >>> t.find("aaabaaa")
        1
        """
        for i in range(1, len(s)):
            if s[i] == s[0] and len(s) % i == 0 and int(len(s)/i) == s.count(s[:i]):
                return int(len(s)/i)

        return 1


if __name__ == '__main__':
    testmod()
