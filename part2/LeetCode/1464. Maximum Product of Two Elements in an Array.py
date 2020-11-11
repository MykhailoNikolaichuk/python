# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        first, second = nums[0] - 1, nums[1] - 1
        return first * second

cl = Solution()
# cl.maxProduct([3,4,5,2])
print('cl.maxProduct([3,4,5,2]): ', cl.maxProduct([3,4,5,2]))


# Given the array of integers nums, you will choose two different indices i and j of that array. 
# Return the maximum value of (nums[i]-1)*(nums[j]-1).
 

# Example 1:

# Input: nums = [3,4,5,2]
# Output: 12 
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 