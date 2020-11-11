# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

from typing import List

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        init_mt = [[0]*m]*n
        for i in indices:
            x = i[0]
            y = i[1]
            init_mt[x] = [j+1 for j in init_mt[x]]
            init_mt[x][y] = [j+1 for j in init_mt[x][y]]
        print(init_mt)
        pass

cl1 = Solution()
# cl1.oddCells()
print('cl1.oddCells(): ', cl1.oddCells(2, 3, [[0,1],[1,1]]))

# Input: n = 2, m = 3, indices = [[0,1],[1,1]]
# Output: 6
# Explanation: Initial matrix = [[0,0,0],
#                                [0,0,0]].
# After applying first increment it becomes [[1,2,1],
#                                            [0,1,0]].
# The final matrix will be [[1,3,1],
#                           [1,3,1]] which contains 6 odd numbers.

# Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where 
# indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

# Return the number of cells with odd values in the matrix after applying the increment to all indices.