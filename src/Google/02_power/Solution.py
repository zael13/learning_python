from doctest import testmod


class Solution:
    def solution(self, xs):
        """
        >>> t = Solution()
        >>> t.solution([2, 0, 2, 2, 0])
        '8'

        >>> t = Solution()
        >>> t.solution([-5])
        '-5'

        >>> t = Solution()
        >>> t.solution([-5, 0, 0])
        '0'

        >>> t = Solution()
        >>> t.solution([-5, 0, 1])
        '1'

        >>> t = Solution()
        >>> t.solution([0, 0])
        '0'

        >>> t = Solution()
        >>> t.solution([0])
        '0'

        >>> t = Solution()
        >>> t.solution([-2, -3, 4, -5])
        '60'
        """
        max_negative = -9999 # absolute value is no greater than 1000
        is_positive_num = False
        res = 0

        for i in xs:
            if i < 0:
                max_negative = max(max_negative, i)
            elif i > 0:
                is_positive_num = True

            if i and res:
                res *= i
            elif i:
                res = i

        if res >= 0 or (res == max_negative and not is_positive_num and len(xs) == 1):
            return str(res)
        elif res < 0 and res == max_negative and not is_positive_num:
            return '0'
        else:
            return str(res // max_negative)


if __name__ == '__main__':
    testmod()
