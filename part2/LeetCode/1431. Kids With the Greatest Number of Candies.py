from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [True if amount + extraCandies >= max_candies else False for amount in candies]

cl = Solution()
print(cl.kidsWithCandies([2,3,5,1,3], 3))

# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 