base_m = ((0,3,2,3,2,3,4,5),
          (3,2,1,2,3,4,3,4),
          (2,1,4,3,2,3,4,5),
          (3,2,3,2,3,4,3,4),
          (2,3,2,3,4,3,4,5),
          (3,4,3,4,3,4,5,4),
          (4,3,4,3,4,5,4,5),
          (5,4,5,4,5,4,5,6))
SIZE = 8


#
class Solution:
    def solution(self, src, dest):
        """
        >>> t = Solution()
        >>> t.solution(0, 1)
        3

        >>> t = Solution()
        >>> t.solution(19, 36)
        1
        """
        src_x = src % SIZE
        src_y = src//SIZE
        dest_x = dest % SIZE
        dest_y = dest//SIZE

        return base_m[abs(dest_y-src_y)][abs(dest_x-src_x)]

if __name__ == '__main__':
    testmod()


#val[y][x] = min(val[y-2][x-1], val[y-2][x+1], val[y-1][x-1], val[y-1][x+1]) + 1