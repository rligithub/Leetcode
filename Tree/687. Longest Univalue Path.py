# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # SIMILAR TO # 543. Diameter of Binary Tree
        # 每一个node返回的相同value的左孩子和右孩子最大值
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if root.left and root.left.val == root.val:
            left += 1
        else:
            left = 0
        if root.right and root.right.val == root.val:
            right += 1
        else:
            right = 0

        self.res = max(self.res, left + right)
        return max(left, right)


class Solution1:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # 每一个node返回的相同value的左孩子和右孩子最大值
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        L, R = 0, 0
        if root.left and root.left.val == root.val:
            L = left + 1
        if root.right and root.right.val == root.val:
            R = right + 1

        self.res = max(self.res, L + R)

        return max(L, R)