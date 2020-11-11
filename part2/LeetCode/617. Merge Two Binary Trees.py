# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
root2 = TreeNode(2, TreeNode(1, right=TreeNode(4)), TreeNode(3, right=TreeNode(7)))

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.value)
        printTree(node.right, level + 1)

# printTree(root1)

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        elif not t2:
            return t1
        else:
            res = TreeNode(t1.value + t2.value)
            res.left = self.mergeTrees(t1.left, t2.left)
            res.right = self.mergeTrees(t1.right, t2.right)
        return res

cl = Solution()
new_tree = cl.mergeTrees(root1, root2)
print('cl.mergeTrees(root1, root2): ', printTree(new_tree))

