from doctest import testmod
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        >>> t = Solution()
        >>> t.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
        [0, 2, 1, 3]
        """
        self.depends_on = [set() for i in range(numCourses)]
        self.prerequisite_for = [set() for i in range(numCourses)]
        self.able_to_take = [i for i in range(numCourses)]
        self.res = []

        for i in prerequisites:
            self.prerequisite_for[i[1]].add(i[0])
            self.depends_on[i[0]].add(i[1])
            if i[0] in self.able_to_take:
                self.able_to_take.remove(i[0])

        while self.able_to_take:
            c = self.able_to_take.pop()
            self.takeTheCourse(c)
            self.res.append(c)

        if len(self.res) == numCourses:
            return self.res
        else:
            return []

    def takeTheCourse(self, idx):
        for c in self.prerequisite_for[idx]:
            self.depends_on[c].remove(idx)
            if len(self.depends_on[c]) == 0:
                self.able_to_take.append(c)


if __name__ == '__main__':
    testmod()
