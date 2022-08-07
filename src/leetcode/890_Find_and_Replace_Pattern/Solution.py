from doctest import testmod
from typing import List
from collections import Counter

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """
        >>> t = Solution()
        >>> t.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb")
        ['mee', 'aqq']

        >>> t = Solution()
        >>> t.findAndReplacePattern(["a","b","c"], "a")
        ['a', 'b', 'c']

        >>> t = Solution()
        >>> t.findAndReplacePattern(["badc","abab","dddd","dede","yyxx"], "baba")
        ['abab', 'dede']

        """

        def mutate(s):
            dictionary = {}
            res = []
            for i in s:
                if i not in dictionary:
                    dictionary[i] = len(dictionary)
                res.append(dictionary[i])

            return res

        p = mutate(pattern)
        out = []
        for i in words:
            if p == mutate(i):
                out.append(i)
        return out




if __name__ == '__main__':
    testmod()
