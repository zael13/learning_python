from doctest import testmod
from typing import List

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        >>> t = Solution()
        >>> t.countVowelPermutation(1)
        5

        >>> t = Solution()
        >>> t.countVowelPermutation(2)
        10

        >>> t = Solution()
        >>> t.countVowelPermutation(5)
        68

        >>> t = Solution()
        >>> t.countVowelPermutation(900)
        85691
        """
        graph = [[1], [0, 2], [0, 1, 3, 4], [2, 4], [0]]

        # @cache
        def dfs(step, idx):
            if step == n-1:
                return 1
            else:
                count = 0
                for i in graph[idx]:
                    count += dfs(step+1, i) % (10**9 + 7)
                return count

        res = 0
        for i in range(len(graph)):
            res += dfs(0, i)

        return res % (10**9 + 7)

if __name__ == '__main__':
    testmod()
