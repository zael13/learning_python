from doctest import testmod


def solve(l, i):
    """
    >>> solve([1,2,3,4,5,6], 3)
    2

    >>> solve([1,2,4,5,6], 2)
    1

    >>> solve([1,2,3,4,5,6], 6)
    5

    >>> solve([1,2,4,5,6], 3)

    """

    return next_step(l, 0, len(l)-1, i)


def next_step(l, left, right, item):
    if left >= right and l[left] != item:
        return None

    mean = int((left+right)/2)
    if l[mean] == item:
        return mean
    elif l[mean] < item:
        return next_step(l, mean+1, right, item)
    else:
        return next_step(l, left, mean-1, item)


if __name__ == '__main__':
    testmod()
