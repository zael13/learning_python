from doctest import testmod
from typing import List
import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        >>> t = Solution()
        >>> t.countSmaller([5,2,6,1])
        [2, 1, 1, 0]

        >>> t = Solution()
        >>> t.countSmaller([6,5,2,1])
        [3, 2, 1, 0]

        >>> t = Solution()
        >>> t.countSmaller([1,2,3,4])
        [0, 0, 0, 0]

        >>> t = Solution()
        >>> t.countSmaller([-1])
        [0]

        >>> t = Solution()
        >>> t.countSmaller([-1])
        [0]

        >>> t = Solution()
        >>> t.countSmaller([-1, -1])
        [0, 0]
        """

        # idxs = []
        # vals = {}
        #
        # for i in range(len(nums)):
        #     if nums[i] not in vals:
        #         bisect.insort(idxs, nums[i])
        #         vals[nums[i]] = {}
        #     vals[nums[i]][i] = 0
        #     j = len(idxs)-1
        #     while idxs[j] > nums[i]:
        #         for k in vals[idxs[j]].keys():
        #             vals[idxs[j]][k] += 1
        #         j-=1
        #
        # res = []
        # for i in range(len(nums)):
        #     res.append(vals[nums[i]][i])
        #
        # return res

        vals = []
        for val in nums:
            bisect.insort(vals, val)

        res = []
        for val in nums:
            idx = bisect.bisect_left(vals, val)
            del vals[idx]
            res.append(idx)

        return res


if __name__ == '__main__':
    testmod()
