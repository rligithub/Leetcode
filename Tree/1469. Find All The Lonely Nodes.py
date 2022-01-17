# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        # only one child --> return list of child.val

        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return

        if root.left and not root.right:
            self.res.append(root.left.val)

        if root.right and not root.left:
            self.res.append(root.right.val)

        self.dfs(root.left)
        self.dfs(root.right)

