from doctest import testmod
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        >>> t = Solution()
        >>> t.combinationSum3(3,7)
        [[1, 2, 4]]

        >>> t = Solution()
        >>> t.combinationSum3(9,45)
        [[1, 2, 3, 4, 5, 6, 7, 8, 9]]

        >>> t = Solution()
        >>> t.combinationSum3(4,1)
        []

        >>> t = Solution()
        >>> t.combinationSum3(3,9)
        [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        """
        self.res = []
        self.k = k
        self.n = n
        self.find(range(1, 10), [], 0)

        return self.res

    def find(self, vals, arr, sum):
        for i in vals:
            # print(f"i: {i}, arr: {arr}, sum: {sum}")
            if i + sum < self.n and len(arr) < self.k-1:
                tmp = arr[:]
                tmp.append(i)
                self.find(range(i+1, 10), tmp, i+sum)
            elif i+sum == self.n and len(arr) == self.k-1:
                tmp = arr[:]
                tmp.append(i)
                self.res.append(tmp)
                break
            elif i+sum > self.n or len(arr) == self.k:
                break



if __name__ == '__main__':
    testmod()
