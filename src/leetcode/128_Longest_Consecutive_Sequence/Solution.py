from doctest import testmod
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        >>> t = Solution()
        >>> t.longestConsecutive([100,4,200,1,3,2])
        4

        >>> t = Solution()
        >>> t.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
        9

        >>> t = Solution()
        >>> t.longestConsecutive([0,3,7,2,5,8,4,6,0,1,11,12,6,7,2,3])
        9


        >>> t = Solution()
        >>> t.longestConsecutive([1,2,0,1])
        3

        """

        ends = dict()
        begins = dict()

        for i in nums:
            if i+1 in ends and i-1 in begins:
                ends[begins[i-1]] = ends[i + 1]
                begins[ends[i+1]] = begins[i - 1]
                del begins[i - 1]
                del ends[i + 1]

                if i + 1 in ends:
                    ends[i] = ends[i+1]
                    del ends[i+1]
                elif i - 1 in begins:
                    begins[i] = begins[i - 1]
                    del begins[i - 1]
            else:
                if i + 1 in ends:
                    ends[i] = ends[i+1]
                    del ends[i+1]
                elif i-1 in ends:
                    ends[i-1] = i
                else:
                    ends[i] = i

                if i - 1 in begins:
                    begins[i] = begins[i - 1]
                    del begins[i - 1]
                elif i+1 in begins:
                    begins[i+1] = i
                else:
                    begins[i] = i
            print(f"i: {i}  begins {begins} ends {ends}")

        res = 0
        for k, v in begins.items():
            res = max(res, k - v + 1)
        for k, v in ends.items():
            res = max(res, v - k + 1)

        return res

if __name__ == '__main__':
    testmod()
