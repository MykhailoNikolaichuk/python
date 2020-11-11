# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

class Solution:
    def generateTheString(self, n: int) -> str:
        DIFF = 97
        ans = ''    
        for _ in range(n - 1):
            ans += chr(DIFF)
        if n % 2 == 0:
            ans += chr(DIFF + 1)
        else:
            ans += chr(DIFF)
        return ans

cl = Solution()
# cl.generateTheString(5)
print('cl.generateTheString(5): ', cl.generateTheString(6))


