from typing import List

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        init_letter = s[0]
        counter = 0
        ans = 0
        for ch in s:
            print('ch: ', ch)
            if ch is init_letter:
                counter += 1
            else:
                counter -= 1
            
            if counter == 0:
                ans += 1
        return ans


cl1 = Solution()
print('cl1.balancedStringSplit("RLRRLLRLRL"): ', cl1.balancedStringSplit("RLLLLRRRLR"))


# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# Given a balanced string s split it in the maximum amount of balanced strings.
# Return the maximum amount of splitted balanced strings.

 
# Example 1:
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

# Example 2:
# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
# Example 3: