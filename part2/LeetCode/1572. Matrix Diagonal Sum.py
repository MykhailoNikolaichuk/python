# https://leetcode.com/problems/matrix-diagonal-sum/

from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans, j, k = 0, 0, len(mat) - 1
        for i in range(len(mat)):
            if k == j:
                ans += mat[i][j]
            else:
                ans += mat[i][j] + mat[i][k]
            j += 1
            k -= 1
        return ans

cl = Solution()
print(cl.diagonalSum([[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]))
