# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([num for num in nums if len(str(num)) % 2 == 0])


cl = Solution()
# cl.findNumbers([12,345,2,6,7896])
print('cl.findNumbers([12,345,2,6,7896]): ', cl.findNumbers([12,345,2,6,7896]))