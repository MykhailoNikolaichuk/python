# https://leetcode.com/problems/unique-morse-code-words/
from typing import List

morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
DIFF = 97

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ans = []
        for word in words:
            cypher_str = ''
            for letter in word:
                cypher_str += morse[ord(letter) - DIFF]
            ans.append(cypher_str)
        return len(list(set(ans)))


cl1 = Solution()
print('cl1.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]): ', cl1.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))