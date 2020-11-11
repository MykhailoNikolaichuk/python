from typing import List


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ans = 0
        for ch in S:
            if ch in J:
                ans += 1
        return ans
    def numJewelsInStones2(self, J: str, S: str) -> int:
        ans = 0
        for ch in J:
                ans += S.count(ch)
        return ans

cl = Solution()
print(cl.numJewelsInStones("aA", "aAAbbbb"))

# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:

# Input: J = "aA", S = "aAAbbbb"
# Output: 3
# Example 2:

# Input: J = "z", S = "ZZ"
# Output: 0