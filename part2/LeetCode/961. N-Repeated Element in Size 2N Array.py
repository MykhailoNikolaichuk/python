# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

from typing import List

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        occurences = {}
        N = len(list(set(A))) - 1
        for item in A:
            if item in occurences:
                occurences[item] += 1
            else:
                occurences[item] = 1

        for key, value in occurences.items():
            if value == N:
                return key

cl = Solution()
print('cl.repeatedNTimes([1,2,3,3]): ', cl.repeatedNTimes([1,2,3,3]))

# Input: [1,2,3,3]
# Output: 3