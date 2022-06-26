import collections
from doctest import testmod
from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """
        >>> t = Solution()
        >>> t.checkPossibility([4,2,3])
        True

        >>> t = Solution()
        >>> t.checkPossibility([1])
        True

        >>> t = Solution()
        >>> t.checkPossibility([1,1,10,1])
        True

        >>> t = Solution()
        >>> t.checkPossibility([10,1,1])
        True

        >>> t = Solution()
        >>> t.checkPossibility([10,10,1,10])
        True

        >>> t = Solution()
        >>> t.checkPossibility([10,10,1,1])
        False

        >>> t = Solution()
        >>> t.checkPossibility([1,10,0,1])
        False

        >>> t = Solution()
        >>> t.checkPossibility([4,2,1])
        False
        """
        decrease = False
        last = nums[0]
        prev = None

        for i in range(1, len(nums)):
            if nums[i] >= last:
                prev = last
                last = nums[i]
            else:
                if decrease:
                    return False
                else:
                    decrease = True

                if prev is None or (last > prev and prev <= nums[i]):
                    last = nums[i]

        return True



if __name__ == '__main__':
    testmod()
