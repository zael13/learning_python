from collections import defaultdict
from doctest import testmod
from typing import List
from functools import lru_cache



class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        >>> t = Solution()
        >>> t.longestStrChain(["a","b","ba","bca","bda","bdca"])
        4

        >>> t = Solution()
        >>> t.longestStrChain(["bdca","bda","ca","dca","a"])
        4

        >>> t = Solution()
        >>> t.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"])
        5

        >>> t = Solution()
        >>> t.longestStrChain(["czgxmxrpx","lgh","bj","cheheex","jnzlxgh","nzlgh","ltxdoxc","bju","srxoatl","bbadhiju","cmpx","xi","ntxbzdr","cheheevx","bdju","sra","getqgxi","geqxi","hheex","ltxdc","nzlxgh","pjnzlxgh","e","bbadhju","cmxrpx","gh","pjnzlxghe","oqlt","x","sarxoatl","ee","bbadju","lxdc","geqgxi","oqltu","heex","oql","eex","bbdju","ntxubzdr","sroa","cxmxrpx","cmrpx","ltxdoc","g","cgxmxrpx","nlgh","sroat","sroatl","fcheheevx","gxi","gqxi","heheex"])
        9

        >>> t = Solution()
        >>> t.longestStrChain(["abcd","dbqca"])
        1
        """
        hist = defaultdict(list)
        for i in range(len(words)):
            hist[len(words[i])].append(i)
        lengths = sorted(hist.keys(), reverse=True)

        max_len = 1 if len(words) else 0
        res = list([i] for i in hist[lengths[0]])

        for i in lengths[:-1]:
            if i-1 in lengths:
                tmp = []
                for z in range(len(res)):
                    for j in hist[i-1]:
                        if self.validate(words[res[z][-1]], words[j]):
                            tmp.append(res[z][:])
                            tmp[-1].append(j)
                            max_len = max(max_len, len(tmp[-1]))
                for j in hist[i - 1]:
                    for z in range(len(tmp)):
                        if tmp[z][-1] == words[j]:
                            break
                    else:
                        tmp.append([j])
                res = tmp
            else:
                res = []
        return max_len

    @lru_cache(None)
    def validate(self, long, short):
        if len(short)+1 != len(long):
            return False
        removed = 0
        for i in range(len(short)):
            if short[i] != long[i+removed] and removed == 0:
                removed += 1
                if short[i] != long[i + removed]:
                    return False
            elif short[i] != long[i+removed] and removed > 0:
                return False
        return True


if __name__ == '__main__':
    testmod()
