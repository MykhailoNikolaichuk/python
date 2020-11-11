# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        subs = [[]]
        for i in range(len(arr)):
            n = i+1
            while n <= len(arr):
                sub = arr[i:n]
                subs.append(sub)
                n += 1
        return sum([sum(x) for x in subs if len(x) % 2 == 1])


cl = Solution()
print('cl.sumOddLengthSubarrays([1,4,2,5,3]): ', cl.sumOddLengthSubarrays([1,4,2,5,3]))

# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58