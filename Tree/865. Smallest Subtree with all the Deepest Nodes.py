# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.maxx = 0
        self.res = root
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, height):
        if not root:
            return -1
        left = self.dfs(root.left, height + 1)
        right = self.dfs(root.right, height + 1)

        if left != -1 and left == right & left >= self.maxx and right >= self.maxx:
            self.res = root
            self.maxx = left
        elif left > right and left > self.maxx:
            self.res = root.left
            self.maxx = left
        elif right > left and right > self.maxx:
            self.res = root.right
            self.maxx = right

        return max(left, max(right, height))


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        maxheight, node = self.dfs(root, 0)
        return node

    def dfs(self, root, height):
        if not root:
            return height, root

        leftH, leftNode = self.dfs(root.left, height + 1)
        righH, rightNode = self.dfs(root.right, height + 1)

        if leftH == righH:
            return leftH, root

        elif leftH > righH:
            return leftH, leftNode
        else:
            return righH, rightNode


