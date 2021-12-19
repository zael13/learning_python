from doctest import testmod


def longest_unique_sequence(str):
    '''
    >>> longest_unique_sequence("adccdb")
    3
    >>> longest_unique_sequence('ccccccc')
    1
    >>> longest_unique_sequence("adcdba")
    4
    '''
    pass


if __name__ == '__main__':
    testmod(name='longest_unique_sequence', verbose=True)
