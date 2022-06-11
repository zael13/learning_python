from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda i:i[0]*i[0]+i[1]*i[1])
        return points[0:k]