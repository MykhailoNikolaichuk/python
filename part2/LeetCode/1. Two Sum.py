from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - value

            if remaining in seen:
                return [i, seen[remaining]]
            else:
                seen[value] = i

cl = Solution()
# cl.twoSum([2,7,11,15])
print('cl.twoSum([2,7,11,15]): ', cl.twoSum([2,7,11,15], 9))

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]