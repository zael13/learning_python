from doctest import testmod


class LongestUniqueSequence:
    def __init__(self):
        self.stored = {}
        self.max_len = 0
        self.p = 0

    def find_len(self, s):
        """
        >>> t = LongestUniqueSequence()
        >>> t.find_len('abccdb')
        3
        >>> t = LongestUniqueSequence()
        >>> t.find_len('cccccccccccc')
        1
        >>> t = LongestUniqueSequence()
        >>> t.find_len("adcdba")
        4
        >>> t = LongestUniqueSequence()
        >>> t.find_len("pwwkew")
        3
        >>> t = LongestUniqueSequence()
        >>> t.find_len("tmmzuxt")
        5
        """
        if len(s) <= 1:
            return len(s)

        for i in range(len(s)):
            if s[i] in self.stored:
                self.p = max(self.stored[s[i]]+1, self.p)
            self.stored[s[i]] = i
            self.max_len = max(self.max_len, i+1 - self.p)

        return self.max_len

if __name__ == '__main__':
    testmod()
