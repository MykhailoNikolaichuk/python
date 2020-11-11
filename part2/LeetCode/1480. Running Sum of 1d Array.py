from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_list = []
        sum = 0
        for x in nums:
            sum += x
            new_list.append(sum)
        return new_list

cl = Solution()
print(cl.runningSum([3,1,2,10,1]))