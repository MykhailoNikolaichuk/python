from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    counter += 1
        return counter


cl = Solution()
print(cl.numIdenticalPairs([1,2,3,1,1,3]))







# Given an array of integers nums.

# A pair (i,j) is called good if nums[i] == nums[j] and i < j.

# Return the number of good pairs.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.