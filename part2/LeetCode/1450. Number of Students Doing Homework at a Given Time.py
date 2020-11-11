# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0
        for i, j in zip(startTime, endTime):
            if i <= queryTime and queryTime <= j:
                ans += 1
        return ans

cl = Solution()
# cl.busyStudent([1,2,3], [3,2,7], 4)
print('cl.busyStudent([1,2,3], [3,2,7], 4): ', cl.busyStudent([1,2,3], [3,2,7], 4))

# Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
# Output: 1
