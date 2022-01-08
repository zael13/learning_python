from doctest import testmod
from typing import List


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        >>> t = Solution()
        >>> t.maxAncestorDiff([8,3,10,1,6,None,14,None,None,4,7,13])
        7

        >>> t = Solution()
        >>> t.maxAncestorDiff([1,None,2,None,0,3])
        3
        """

        self.v = 0
        self.maxDiff(root, [root.val, root.val])
        return self.v

    def maxDiff(self, node, diff):
        if not node:
            return

        if node.val < diff[0]:
            diff = [node.val, diff[1]]
            self.v = max(self.v, diff[1] - diff[0])
        elif node.val > diff[1]:
            diff = [diff[0], node.val]
            self.v = max(self.v, diff[1] - diff[0])

        self.maxDiff(node.left, diff)
        self.maxDiff(node.right, diff)


if __name__ == '__main__':
    testmod()
