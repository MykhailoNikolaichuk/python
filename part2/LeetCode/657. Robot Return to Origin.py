# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        coord = {
            'x' : 0,
            'y' : 0
        }
        for letter in moves:
            if letter == 'U':
                coord['x'] += 1
            elif letter == 'D':
                coord['x'] -= 1
            elif letter == 'R':
                coord['y'] += 1
            elif letter == 'L':
                coord['y'] -= 1
        if coord['x'] == 0 and coord['y'] == 0:
            return True
        else:
            return False

cl = Solution()
print('cl.judgeCircle("UD"): ', cl.judgeCircle('UD'))
# Input: moves = "UD"
# Output: true