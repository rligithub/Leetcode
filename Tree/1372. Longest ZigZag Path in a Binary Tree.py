# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
direction:
0 - left
1 - right

"""


class Solution:  # ok
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return -1
        self.res = -1
        self.dfs(root.left, 0, 0)
        self.dfs(root.right, 1, 0)
        return self.res

    def dfs(self, root, direction, count):

        if not root:
            self.res = max(self.res, count)
            return

        if direction == 1:
            self.dfs(root.left, 0, count + 1)
            self.dfs(root.right, 1, 0)
        if direction == 0:
            self.dfs(root.left, 0, 0)
            self.dfs(root.right, 1, count + 1)


class Solution1:  best


def longestZigZag(self, root: TreeNode) -> int:
    self.res = 0
    self.dfs(root)
    return self.res


def dfs(self, node):
    if not node:
        return -1, -1  # L_cnt, R_cnt

    L2L, L2R = self.dfs(node.left)
    R2L, R2R = self.dfs(node.right)

    self.res = max(self.res, L2R + 1, R2L + 1)

    return L2R + 1, R2L + 1  # R_cnt, L_cnt