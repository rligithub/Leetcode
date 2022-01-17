# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # print in-order traversal, reconstruct the balanced binary search tree
        self.res = []
        self.dfs(root)
        return self.construct(self.res)

    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)
        self.res.append(root.val)
        self.dfs(root.right)

    def construct(self, num):
        if not num:
            return

        mid = len(num) // 2

        root = TreeNode(num[mid])
        root.left = self.construct(num[:mid])
        root.right = self.construct(num[mid + 1:])

        return root


class SolutionTony:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        self.dfs(root, inorder)
        return self.buildBST(inorder)

    def buildBST(self, inorder):
        if not inorder:
            return None

        mid = (len(inorder)) // 2
        root = TreeNode(inorder[mid])
        root.left = self.buildBST(inorder[:mid])
        root.right = self.buildBST(inorder[mid + 1:])
        return root

    def dfs(self, root, res):
        if not root:
            return None
        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)