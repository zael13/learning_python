from doctest import testmod

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        >>> t = Solution()
        >>> t.backspaceCompare("aaab#c", "aaacb#")
        True

        >>> t = Solution()
        >>> t.backspaceCompare("abc#d#",  "ab")
        True


        >>> t = Solution()
        >>> t.backspaceCompare("###a", "a")
        True

        >>> t = Solution()
        >>> t.backspaceCompare("ab#c", "ad#c")
        True

        >>> t = Solution()
        >>> t.backspaceCompare("ab##", "c#d#")
        True

        >>> t = Solution()
        >>> t.backspaceCompare("aaaaaa###a", "aa")
        False

        >>> t = Solution()
        >>> t.backspaceCompare("a#c", "b")
        False


        >>> t = Solution()
        >>> t.backspaceCompare("abc", "abc#")
        False
        """
        p1 = len(s)-1
        p2 = len(t)-1
        while (p1 >= 0 or p2 >= 0) :
            if s[p1] == "#" or t[p2] == "#":
                if s[p1] == "#":
                    b = 2
                    while b and p1 >= 0:
                        p1 -= 1
                        b -= 1
                        if s[p1] == "#":
                            b += 2

                if t[p2] == "#":
                    b = 2
                    while b and p2 >= 0:
                        p2 -= 1
                        b -= 1
                        if t[p2] == "#":
                            b += 2
            else:
                if s[p1] != t[p2]:
                    return False
                else:
                    p1 -= 1
                    p2 -= 1

        return True





if __name__ == '__main__':
    testmod()
