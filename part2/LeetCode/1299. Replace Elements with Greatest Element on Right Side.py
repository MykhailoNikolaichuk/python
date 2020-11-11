# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        tmp_arr = arr.copy()
        for i, number in enumerate(arr):
            tmp_arr.pop(0)
            if len(tmp_arr) == 0:
                ans.append(-1)    
            else:
                ans.append(max(tmp_arr))
            
        return ans

cl = Solution()
print('cl.replaceElements([17,18,5,4,6,1]): ', cl.replaceElements([17,18,5,4,6,1]))

# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]