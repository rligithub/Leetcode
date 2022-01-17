# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # pre-order --> if root.val == even, find grandkid, sum ++
        self.summ = 0
        self.dfs(root)
        return self.summ

    def dfs(self, root):
        if not root:
            return

        if root.val % 2 == 0:
            if root.left:
                if root.left.left:
                    self.summ += root.left.left.val
                if root.left.right:
                    self.summ += root.left.right.val
            if root.right:
                if root.right.left:
                    self.summ += root.right.left.val
                if root.right.right:
                    self.summ += root.right.right.val

        self.dfs(root.left)
        self.dfs(root.right)


class Solution2:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # pre-order --> if root.val == even, find grandkid, sum ++

        return self.dfs(root, 0, 0)

    def dfs(self, root, parent, grandparent):
        if not root:
            return 0
        left = self.dfs(root.left, root.val, parent)
        right = self.dfs(root.right, root.val, parent)

        if grandparent != 0 and grandparent % 2 == 0:
            return root.val + left + right
        else:
            return left + right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # pre-order --> if root.val == even, find grandkid, sum ++
        self.summ = 0
        self.dfs(root, 0, 0)
        return self.summ

    def dfs(self, root, parent, grandparent):
        if not root:
            return 0
        self.dfs(root.left, root.val, parent)
        self.dfs(root.right, root.val, parent)

        if grandparent != 0 and grandparent % 2 == 0:
            self.summ += root.val
