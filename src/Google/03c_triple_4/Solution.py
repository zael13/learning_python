from collections import defaultdict

def solution(l):
    """
    >>> solution([1, 2, 3, 4, 5, 6])
    3

    >>> solution([1, 2, 3, 4, 5, 8, 10])
    6

    >>> solution([1, 2, 3, 4, 4, 3, 2, 1])
    6

    >>> solution([1, 1 ,1])
    1

    >>> solution([5, 7 ,11, 23, 111])
    0

    >>> solution([1, 1])
    0

    >>> solution([5,4,3,2,1])
    0

    >>> solution([1, 1 ,1, 1])
    4

    """
    p1_cnt, p3_cnt, res = 0, 0, 0

    for i in range(1, len(l) - 1):
        for j in range(i):
            if l[i] % l[j] == 0:
                p1_cnt += 1
        for j in range(i+1, len(l)):
            if l[j] % l[i] == 0:
                p3_cnt += 1
        res += p1_cnt * p3_cnt
        p1_cnt, p3_cnt = 0, 0
    return res


if __name__ == '__main__':
    testmod()