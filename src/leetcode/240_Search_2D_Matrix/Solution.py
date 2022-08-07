from doctest import testmod
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        >>> t = Solution()
        >>> t.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)
        True

        >>> t = Solution()
        >>> t.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20)
        False

        >>> t = Solution()
        >>> t.searchMatrix([[1]], 20)
        False

        >>> t = Solution()
        >>> t.searchMatrix([[1]], 1)
        True

        >>> t = Solution()
        >>> t.searchMatrix([[1, 3]], 3)
        True
        """

        def dfs(y_min, y_max, x_min, x_max):
            if matrix[y_min][x_min] > target:
                return False

            steps = min(y_max - y_min, x_max - x_min) + 1

            for i in range(steps):
                print(matrix[y_min+i][x_min+i])
                if matrix[y_min+i][x_min+i] == target:
                    return True
                elif matrix[y_min+i][x_min+i] > target:
                    return dfs(y_min + i, y_max, x_min, x_min + i) or dfs(y_min, y_min + i, x_min + i, x_max)

            # print(matrix[y_min+i][x_min+i])
            if y_max - y_min > x_max - x_min:
                # print(f"down y_min {y_min + steps}, y_max {y_max}, x_min {x_min}, x_max {x_max}")
                return dfs(y_min + steps, y_max, x_min, x_max)
            elif y_max - y_min < x_max - x_min:
                # print(f"right y_min {y_min}, y_max {y_max}, x_min {x_min + steps}, x_max {x_max}")
                return dfs(y_min, y_max, x_min + steps, x_max)
            else:
                return False

        return dfs(0, len(matrix)-1, 0, len(matrix[0])-1)


if __name__ == '__main__':
    testmod()
