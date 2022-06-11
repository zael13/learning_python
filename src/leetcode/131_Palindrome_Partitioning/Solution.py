import collections
from doctest import testmod
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # The idea here is to search for all palindromes and form a dict palindrome[start_index] = [end_indexes].
        # We will start evaluation for each i counted as a middle of substring to avoid multiple avaluation of the same substing.
        # In a such way we will have time complexity here: O((N x N/2))
        self.pol = collections.defaultdict(list)
        for i in range(len(s)):
            # Collect even and odd palindromes
            self.findPol(i, i, s)
            self.findPol(i, i+1, s)

        # When the dict if formed we can loop for each item where start_index is the same as
        # last_index + 1 of already generated result and append the value.
        # Time complexity here: O((N x 2^N))
        self.out = []
        self.genOut([], 0, s)

        return self.out

    def findPol(self, left, right, s):
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                self.pol[left].append(right)
                left -= 1
                right += 1
            else:
                break

    def genOut(self, res, idx, s):
        if idx >= len(s):
            self.out.append(res)
            return
        for p in self.pol[idx]:
            tmp = res[:]
            tmp.append(s[idx:p+1])
            self.genOut(tmp, p+1, s)


    if __name__ == '__main__':
        testmod()
