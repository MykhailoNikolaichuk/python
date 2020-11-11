# https://leetcode.com/problems/to-lower-case/

class Solution:
    def toLower(self, ch):
        o = ord(ch)
        return chr(o + 32) if 64<o<91 else ch

    def toLowerCase(self, str: str) -> str:
        return ''.join([self.toLower(ch) for ch in str])

cl = Solution()
# cl.toLowerCase("Hello")
print('cl.toLowerCase("Hello"): ', cl.toLowerCase("Hello"))