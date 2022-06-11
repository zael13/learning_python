from doctest import testmod
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        >>> t = Solution()
        >>> t.maxCoins([3,1,5,8])
        167

        >>> t = Solution()
        >>> t.maxCoins([1,5])
        10
        """
        self.balls = {}

        for i in range(1, len(nums)-1):
            self.balls[i] = (nums[i], i-1, i+1)

        self.balls[0] = (nums[0], None, 1)
        self.balls[len(nums) - 1] = (nums[len(nums) - 1], len(nums) - 2, None)
        print(self.balls)


        for i in range(len(self.balls)):
             self.calcBallSum(self.balls[i])
        #
        # while(self.balls):
        #     maxVal = max(self.balls, key=sum)
        #     self.burstBallon(maxVal)
        #     del self.balls[maxVal]

    # def getVal(self, idx):
    #     if idx is None or idx < 0 or idx > len(self.nums) - 1:
    #         return 1
    #     else:
    #         return self.nums[idx]

    def calcBallSum(self, idx):
        prevPrev = self.balls[idx][1]prev.val if ball.prev and ball.prev.prev else 1
        nextNext = ball.next.next.val if ball.next and ball.next.next else 1
        prev = ball.prev.val if ball.prev else 1
        next = ball.next.val if ball.next else 1
        ball.sum = (max(prevPrev, nextNext) + ball.val) * next * prev

    def burstBallon(self, ball):
        if ball.next:
            ball.next.prev = ball.prev
        if ball.prev:
            ball.prev.next = ball.next

if __name__ == '__main__':
    testmod()
