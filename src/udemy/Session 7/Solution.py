import re

def solution(s):
    """
    >>> solution("aabaa")
    True

    >>> solution("aabbaa")
    True

    >>> solution("abc")
    False

    >>> solution("a")
    True

    >>> solution("")
    True

    >>> solution("A man, a plan, a canal: Panama")
    True
    """
    # tmp = re.sub("[^A-Za-z0-9]", "", s).lower()
    pattern = re.compile('[\W_]+')
    tmp = pattern.sub('', s).lower()

    # return True if tmp == tmp[::-1] else False

    left, right = 0, len(tmp) - 1

    while left < right:
        if tmp[left] != tmp[right]:
            return False
        left += 1
        right -= 1

    return True

if __name__ == '__main__':
    testmod()