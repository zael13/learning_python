from doctest import testmod


def solve(l):
    """
    >>> solve([1,2,9,5,3,4])
    [1, 2, 3, 4, 5, 9]

    >>> solve([1,2,4,4,23,1,23432,2,3434,234,34,2,3])
    [1, 1, 2, 2, 2, 3, 4, 4, 23, 34, 234, 3434, 23432]

    >>> solve([1])
    [1]

    >>> solve([])
    []
    """
    next_step(l, 0, len(l)-1)

    return l


def next_step(l, left, right):
    if right - left < 1:
        return

    p = right
    i = left
    while i < p:
        if l[i] > l[p]:
            if p-i > 1:
                l[p], l[p-1], l[i] = l[i], l[p], l[p-1]
            else:
                l[p], l[i] = l[i], l[p]
            p -= 1
            continue
        i += 1

    next_step(l, left, p-1)
    next_step(l, p+1, right)

if __name__ == '__main__':
    testmod()
