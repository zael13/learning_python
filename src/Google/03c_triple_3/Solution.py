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
        for j in range(i, len(idx)):
            if idx[j] % idx[i] == 0:
                for z in range(j, len(idx)):
                    if idx[z] % idx[j] == 0:
                        res += calc_tuples(hist[idx[i]], hist[idx[j]], hist[idx[z]])
    return res


def calc_tuples(first, second, third):
    if first[0] > third[-1] or first[0] > second[-1] or second[0] > third[-1]:
        return 0
    p2, p3 = 0, 0
    res = 0
    for i in range(len(first)):
        p2_min = False
        for j in range(p2, len(second)):
            if second[j] > first[i]:
                if not p2_min:
                    p2 = j
                    p2_min = True
                for z in range(p3, len(third)):
                    if third[z] > second[j]:
                        p3 = z
                        res += len(third) - z
                        break
    return res


if __name__ == '__main__':
    testmod()