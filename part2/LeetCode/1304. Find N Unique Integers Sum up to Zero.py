# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [0]
        if n == 1:
            return ans
        elif n % 2 == 0:
            ans = []

        cnt = 1
        for _ in range(int(n / 2)):
            ans.append(cnt, cnt * (-1))
            cnt += 1
        return ans


cl = Solution()
# cl.sumZero(2)
print('cl.sumZero(2): ', cl.sumZero(7))