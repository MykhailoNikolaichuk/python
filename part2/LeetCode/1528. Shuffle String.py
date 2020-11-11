
from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        lst = sorted(list(zip(s, indices)), key=lambda x: x[1])
        return ''.join([b_tup[0] for b_tup in lst])

cl = Solution()
print(cl.restoreString("codeleet", [4,5,6,7,0,2,1,3]))


# Given a string s and an integer array indices of the same length.

# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.

# Example 1:
# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.