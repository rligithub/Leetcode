# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:  # two recursive
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

            # 检查左孩子是不是balanced
        if not self.isBalanced(root.left):
            return False
        # 检查右孩子是不是balanced
        if not self.isBalanced(root.right):
            return False

        # 怎么检查 --> doing something 每层
        return abs(self.maxheight(root.left) - self.maxheight(root.right)) < 2

    def maxheight(self, root):
        if not root:
            return 0

        left = self.maxheight(root.left)
        right = self.maxheight(root.right)

        return max(left, right) + 1


class Solution:  # one recursive
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs返回两个值，只需要一个值
        balanced, height = self.dfs(root)
        return balanced

    def dfs(self, root):
        if not root:
            return True, 0

            # 两个值的recursive
        leftB, leftH = self.dfs(root.left)
        rightB, rightH = self.dfs(root.right)

        # 其中返回的值的定义 --> do something
        height = max(leftH, rightH) + 1

        # 另一个返回值的定义
        if not leftB or not rightB:
            return False, height

        return abs(leftH - rightH) < 2, height




