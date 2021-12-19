from doctest import testmod


class LongestUniqueSequence:
    def __init__(self):
        self.stored = set()
        self.max_len = 0
        self.p = 0

    def find_len(self, s):
        '''
        >>> t = LongestUniqueSequence()
        >>> t.find_len('abccdb')
        3
        >>> t = LongestUniqueSequence()
        >>> t.find_len('cccccccccccc')
        1
        >>> t = LongestUniqueSequence()
        >>> t.find_len("adcdba")
        4
        '''
        for i in range(len(s)):
            if s[i] in self.stored:
                self.remove_until(s, self.p, i)
            else:
                self.stored.add(s[i])
                self.max_len = max(self.max_len, len(self.stored))

        return self.max_len

    def remove_until(self, s, p0, p1):
        for i in range(p0, p1):
            if s[i] != s[p1]:
                self.stored.remove(s[i])
            else:
                self.p = i+1
                break


if __name__ == '__main__':
    testmod()
