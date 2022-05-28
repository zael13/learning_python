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
                                if idx[z] % idx[j] == 0:
                                    for third_idx in range(len(hist[idx[z]])):
                                        if hist[idx[z]][third_idx] > second:
                                            res += len(hist[idx[z]]) - third_idx
                                            break
    return res


if __name__ == '__main__':
    testmod()