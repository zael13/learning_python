#
class Solution:
    def solution(self, n):
        """
        >>> t = Solution()
        >>> t.solution('4')
        2

        >>> t = Solution()
        >>> t.solution('23')
        6

        >>> t = Solution()
        >>> t.solution('11')
        5

        >>> t = Solution()
        >>> t.solution('16')
        4

        >>> t = Solution()
        >>> t.solution('1')
        0

        >>> t = Solution()
        >>> t.solution('15')
        5
        """
        return find_1(int(n))
        # for i in range(1,100):
        #     if find_1(i) != find_2(i):
        #         print("i: {} my: {} other: {}".format(i, find_1(int(i)), find_2(int(i))))

def find_1(n):
    res = 0
    while n != 1:
        if n & 1 == 1:
            if n & 2 == 2 and n != 3:
                n += 1
            else:
                n -= 1
        else:
            n >>= 1
        res += 1

    return res

def find_2(n):
    res = 0
    while n != 1:
        if n & 1 == 1:
            low_p = (n + 1) & ~(n + 1 - 1)
            low_m = (n - 1) & ~(n - 1 - 1)
            if low_m > low_p or low_m == n - 1:
                n-=1
            else:
                n+=1
        else:
            n >>= 1
        res += 1

    return res


if __name__ == '__main__':
    # testmod()
    t = Solution()
    t.solution('4')

#val[y][x] = min(val[y-2][x-1], val[y-2][x+1], val[y-1][x-1], val[y-1][x+1]) + 1