from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        mapping = {}
        result = []
        print(f'== first loop')
        for i in range(len(temp)):
            print(f'> i={i} temp[i]={temp[i]} mapping={mapping}')
            if temp[i] not in mapping:
                mapping[temp[i]] = i
        print(f'>>{mapping}')

        print(f'== second loop')
        for i in range(len(nums)):
            print(f'> i={i} temp[i]={nums[i]} mapping={mapping[nums[i]]}')
            result.append(mapping[nums[i]])
        return result


cl = Solution()
print(cl.smallerNumbersThanCurrent([8,1,2,2,3]))



# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

# Example 1:
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

# Example 2:
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]