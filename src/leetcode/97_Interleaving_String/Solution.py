from doctest import testmod
from typing import List


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        >>> t = Solution()
        >>> t.isInterleave("aabcc", "dbbca", "aadbbcbcac")
        True

        >>> t = Solution()
        >>> t.isInterleave("aabcc", "dbbca", "aadbbbaccc")
        False

        >>> t = Solution()
        >>> t.isInterleave("aabcc", "dbbca", "aadbbcbcac")
        True

        >>> t = Solution()
        >>> t.isInterleave("", "", "")
        True

        >>> t = Solution()
        >>> t.isInterleave("", "a", "a")
        True

        >>> t = Solution()
        >>> t.isInterleave("aabd", "abdc", "aabdabcd")
        True

        >>> t = Solution()
        >>> t.isInterleave("", "", "a")
        False
        """

        if len(s3) != len(s1) + len(s2):
            return False

        return check_path(s1, s2, s3, 0, 0, 0)

# @cache
def check_path(s1, s2, s3, p1, p2, p3):
    for i in range(p3, len(s3)):
        choose_s1, choose_s2 = False, False

        if p1 < len(s1) and s1[p1] == s3[i]:
            choose_s1 = check_path(s1, s2, s3, p1 + 1, p2, i + 1)
        if p2 < len(s2) and s2[p2] == s3[i]:
            choose_s2 = check_path(s1, s2, s3, p1, p2 + 1, i + 1)
        return choose_s1 or choose_s2

    return True
if __name__ == '__main__':
    testmod()
