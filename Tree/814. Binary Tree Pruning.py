# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # post order --> check if left, if right, if root.val == 1
        if self.dfs(root):
            return root
        else:
            None  # if all not contains '1' --> all deleted --> return None

    def dfs(self, root):  # if contains '1' --> operation
        if not root:
            return False

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if not left:  # if left subtree != 1
            root.left = None

        if not right:  # if right subtree != 1
            root.right = None

        return root.val == 1 or left or right 