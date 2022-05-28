from collections import defaultdict


class Solution:
    def solution(self, l):
        """
        >>> t = Solution()
        >>> t.solution([1, 2, 3, 4, 5, 6])
        3

       >>> t = Solution()
        >>> t.solution([1, 2, 3, 4, 5, 8, 10])
        6

       >>> t = Solution()
        >>> t.solution([1, 2, 3, 4, 4, 3, 2, 1])
        6

        >>> t = Solution()
        >>> t.solution([1, 1 ,1])
        1

        >>> t = Solution()
        >>> t.solution([5, 7 ,11, 23, 111])
        0

        >>> t = Solution()
        >>> t.solution([1, 1])
        0

        >>> t = Solution()
        >>> t.solution([5,4,3,2,1])
        0

        >>> t = Solution()
        >>> t.solution([1, 1 ,1, 1])
        4

        """
        hist = defaultdict(list, [])
        for i in range(len(l)):
            hist[l[i]].append(i)

        idx = hist.keys()
        idx.sort()

        res = 0
        for i in range(len(idx)):
            for first in hist[idx[i]]:
                for j in range(i, len(idx)):
                    if idx[j] % idx[i] == 0:
                        for second in hist[idx[j]]:
                            if second > first:
                                for z in range(j, len(idx)):
                                    for third in hist[idx[z]]:
                                        if idx[z] % idx[j] == 0 and third > second:
                                            # res.append((idx[i], idx[j], idx[z]))
                                            res += 1
        return res


if __name__ == '__main__':
    testmod()