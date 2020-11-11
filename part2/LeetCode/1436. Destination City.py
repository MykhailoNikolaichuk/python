# https://leetcode.com/problems/destination-city/

from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        for idx in range(len(paths)):
            found = False
            destination = paths[idx][1]
            for path in paths:
                outgoing = path[0]
                if destination == outgoing:
                    found = True    
                    break

            if not found:
                return destination


cl = Solution()
# cl.destCity(["London","New York"],["New York","Lima"],["Lima","Sao Paulo"])
print(cl.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))