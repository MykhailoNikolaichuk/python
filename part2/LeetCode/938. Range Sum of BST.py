# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        return sum([el for el in root.val if el >= L and el <= R])

t1 = TreeNode([10,5,15,3,7,18], 7, 15)
s1 = Solution()
print('s1.rangeSumBST(t1, 7, 15): ', s1.rangeSumBST(t1, 7, 15))


# root = [10,5,15,3,7,null,18], L = 7, R = 15