from doctest import testmod

class Solution:
    def decodeString(self, s: str) -> str:
        """
        >>> t = Solution()
        >>> t.decodeString("3[a2[c]]")
        'accaccacc'

        >>> t = Solution()
        >>> t.decodeString("2[abc]3[cd]ef")
        'abcabccdcdcdef'

        >>> t = Solution()
        >>> t.decodeString("abc3[cd]xyz")
        'abccdcdcdxyz'

        >>> t = Solution()
        >>> t.decodeString("3[a]2[bc]")
        'aaabcbc'


        """
        self.p = 0
        return self.unwrap(s, 1)

    def unwrap(self, s, num):
        res = ""
        digit = 0
        while self.p < len(s) and s[self.p] != "]":
            if s[self.p] == "[":
                self.p += 1
                res += self.unwrap(s, digit)
                digit = 0
            elif s[self.p].isdigit():
                digit = 10*digit + int(s[self.p])
            else:
                res += s[self.p]
            self.p += 1

        return res*num

if __name__ == '__main__':
    testmod()
