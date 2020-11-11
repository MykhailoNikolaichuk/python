# https://leetcode.com/problems/self-dividing-numbers/

from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right + 1):
            if i == i % 10:
               ans.append(i)
               continue
            elif '0' not in str(i):
                flag = True
                for num in str(i):
                    if i % int(num) != 0:
                        flag = False
                if flag:
                    ans.append(i)

        return ans

cl = Solution()
# cl.selfDividingNumbers(1, 22)
print('cl.selfDividingNumbers(1, 22): ', cl.selfDividingNumbers(1, 22))

# Input: 
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]