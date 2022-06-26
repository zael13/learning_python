from doctest import testmod


def solve(l, i):
    """
    >>> solve([1,2,3,3,5,5,5,6,6], 5)
    (4, 6)
    """
    res, left, right = find_res(l, 0, len(l) - 1, i)

    p1 = res
    p2 = res
    while p1 and l[p1-1] == i:
        p1, left, _ = find_res(l, left, p1-1, i)
    while p2 < len(l)-1 and l[p2+1] == i:
        p2, _, right = find_res(l, p2+1, right, i)

    if p1 and p2:
        return p1, p2
    else:
        return None


def find_res(l, left, right, i):
    while left <= right:
        mean = int((left + right) / 2)
        if l[mean] == i:
            return mean, left, right
        elif l[mean] < i:
            left = mean + 1
        else:
            right = mean - 1

    return None


if __name__ == '__main__':
    testmod()
