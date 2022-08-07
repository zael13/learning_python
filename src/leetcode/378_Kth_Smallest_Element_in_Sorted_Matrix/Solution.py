from doctest import testmod
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        >>> t = Solution()
        >>> t.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8)
        13
        """
        width = len(matrix[0])
        y, x = 0, width - 1
        idx = y * width + x
        prev_idx = idx
        while idx < k-1:
            prev_idx = idx
            idx = y * width + x
            y += 1
        print(f"prev {prev_idx} idx {idx}")

if __name__ == '__main__':
    testmod()
