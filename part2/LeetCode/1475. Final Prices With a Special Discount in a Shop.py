# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i in range(len(prices)):
            discount = 0
            for j in range(len(prices)):
                if j > i and prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            ans.append(prices[i] - discount)
        return ans

cl = Solution()
print('cl.finalPrices([8,4,6,2,3]): ', cl.finalPrices([8,4,6,2,3]))


# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]