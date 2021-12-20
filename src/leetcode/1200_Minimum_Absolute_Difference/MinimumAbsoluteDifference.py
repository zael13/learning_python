from doctest import testmod
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        """
        >>> t = Solution()
        >>> t.minimumAbsDifference([4,2,1,3])
        [[1, 2], [2, 3], [3, 4]]

        >>> t = Solution()
        >>> t.minimumAbsDifference([1,3,6,10,15])
        [[1, 3]]

        >>> t = Solution()
        >>> t.minimumAbsDifference([3,8,-10,23,19,-4,-14,27])
        [[-14, -10], [19, 23], [23, 27]]
        """
        arr.sort()
        min_diff = arr[1]-arr[0]
        res = []

        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff < min_diff:
                min_diff = diff
                res = [arr[i]]
            elif diff == min_diff:
                res.append(arr[i])

        return [[i, i+min_diff] for i in res]


if __name__ == '__main__':
    testmod()
