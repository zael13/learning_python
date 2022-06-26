from doctest import testmod
from typing import List


class Node:
    def __init__(self, val):
        self.min_3 = []
        self.childs = dict()
        self.val = val

    def add_child(self, val):
        self.childs[val] = Node(val)
        if len(self.min_3) < 3:
            self.min_3.append(val)
            self.min_3.sort()
        else:
            if val < self.min_3[-1]:
                self.min_3[-1] = val
                self.min_3.sort()
        print(self.min_3)


def push_word(node, word, idx):
    if idx == len(word):
        node.add_child('\n')
        return
    elif word[idx] not in node.childs:
        node.add_child(word[idx])

    node = node.childs[word[idx]]

    push_word(node, word, idx+1)


def search(node, word, idx):
    if idx < len(word):
        if word[idx] in node.childs:
            return [node.val+i for i in search(node.childs[word[idx]], word, idx+1)]
        else:
            return []
    else:
        tmp = get_sub_nodes(node, '', [])
        return tmp


def get_sub_nodes(node, postfix, res):
    if not node.childs.keys():
        res.append(postfix)
    else:
        for i in node.min_3:
            get_sub_nodes(node.childs[i], postfix+node.val, res)
            if len(res) == 3:
                return res
    return res


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        >>> t = Solution()
        >>> t.suggestedProducts(['mobile','mouse','moneypot','monitor','mousepad'], 'mouse')
        [['mobile', 'moneypot', 'monitor'], ['mobile', 'moneypot', 'monitor'], ['mouse', 'mousepad'], ['mouse', 'mousepad'], ['mouse', 'mousepad']]

        >>> t = Solution()
        >>> t.suggestedProducts(['bags','baggage','banner','box','cloths'], 'bags')
        [['baggage', 'bags', 'banner'], ['baggage', 'bags', 'banner'], ['baggage', 'bags'], ['bags']]

        >>> t = Solution()
        >>> t.suggestedProducts(['havana'], 'havana')
        [['havana'], ['havana'], ['havana'], ['havana'], ['havana'], ['havana']]
        """
        root = Node('')
        for product in products:
            push_word(root, product, 0)

        res = []
        for i in range(1, len(searchWord)+1):
            res.append(search(root, searchWord[:i], 0))
        return res


if __name__ == '__main__':
    testmod()
