# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        final_str, counter = '', 0
        for ch in S:
            if ch == ')': counter -= 1
            if counter != 0: final_str += ch
            if ch == '(': counter += 1
        return final_str

cl = Solution()
# cl.removeOuterParentheses('(()())(())')
print( cl.removeOuterParentheses('(()())(())'))

# Input: "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".