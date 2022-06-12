# https://leetcode.com/problems/container-with-most-water/

# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical
# lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which,
# together with the x-axis forms a container, such that the container contains the most water.
#
# Notice that you may not slant the container.

from typing import List


class Solution:
    """"
    >>> res = Solution()

    >>> res.maxArea([])
    0

    >>> res.maxArea([1])
    0

    >>> res.maxArea([1,8,6,2,5,4,8,3,7])
    49
    """
    def maxArea(self, height: List[int]) -> int:
        max_value = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                area = min(height[i], height[j]) * (j-i)
                max_value = area if area > max_value else max_value
        return max_value


if __name__ == '__main__':
    import doctest
    doctest.testmod()
