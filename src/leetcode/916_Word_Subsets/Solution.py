from doctest import testmod
from typing import List
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        >>> t = Solution()
        >>> t.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"])
        ['facebook', 'google', 'leetcode']

        >>> t = Solution()
        >>> t.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["l","e"])
        ['apple', 'google', 'leetcode']
        """
        c2 = Counter()
        for w2 in words2:
            for k, v in Counter(w2).items():
                c2[k] = max(c2[k], v)

        res = []
        for w1 in words1:
            c1 = Counter(w1)
            for k, v in c2.items():
                if c1[k] < v:
                    break
            else:
                res.append(w1)
        return res

if __name__ == '__main__':
    testmod()
