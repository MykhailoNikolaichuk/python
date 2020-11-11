# https://leetcode.com/problems/minimum-time-visiting-all-points/

from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        steps = 0
        for i in range(len(points)-1):
            print(f'i {i}')
            point = points[i]
            next_point = points[i+1]
            print(abs(next_point[0] - point[0]))
            print(abs(next_point[1] - point[1]))
            steps += max(abs(next_point[0] - point[0]), abs(next_point[1] - point[1]))
            print(f'asd {steps}')
        return steps
                
        

cl = Solution()
print(cl.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
# print('cl.minTimeToVisitAllPoints([[3,2],[-2,2]]): ', cl.minTimeToVisitAllPoints([[3,2],[-2,2]]))
# 5
