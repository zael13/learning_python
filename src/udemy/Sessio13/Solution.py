from doctest import testmod


def solve(s):
    """
    >>> solve('a(b(c)c')
    'ab(c)c'

    >>> solve('))((')
    ''

    >>> solve('(())')
    '(())'

    >>> solve('ab(c)(c')
    'ab(c)c'

    """
    stack = []
    res = []
    for i in range(len(s)):
        if s[i] == ")" and stack:
            stack.pop()
        elif s[i] == ")" and not stack:
            res.append('')
            continue
        elif s[i] == "(":
            stack.append(i)
        res.append(s[i])

    for i in stack:
        res[i] = ''

    return ''.join(res)

if __name__ == '__main__':
    testmod()
