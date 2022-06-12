import re

def solution(s):
    """
    >>> solution("aabaa")
    True

    >>> solution("abccdba")
    True

    >>> solution("abcdefdba")
    False

    >>> solution("a")
    True

    >>> solution("ab")
    True

    >>> solution("")
    True
    """
    pattern = re.compile('[\W_]+')
    tmp = pattern.sub('', s).lower()

    left, right = 0, len(tmp) - 1
    removed = False

    while left < right:
        if tmp[left] != tmp[right]:
            if removed:
                return False
            else:
                if tmp[left] == tmp[right-1]:
                    right -= 1
                elif tmp[left+1] == tmp[right]:
                    left += 1
                else:
                    return False
                removed = True
                
        left += 1
        right -= 1

    return True

if __name__ == '__main__':
    testmod()