# https://leetcode.com/problems/flipping-an-image/

from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        ans = []
        for line in A:
            ans.append([0 if x == 1 else 1 for x in reversed(line)])
        return ans

cl = Solution()
# cl.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
print('cl.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]): ', cl.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))

# [[1,0,0],[0,1,0],[1,1,1]]