# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # left_head --> root.left ; left_tail --> lastL
        # right_head --> root.right ; right_tail --> lastR

        if not root:
            return None

        lastL = self.flatten(root.left)
        lastR = self.flatten(root.right)

        if lastL:
            lastL.right = root.right  # left_linkedlist_tail connected to right_linkedlist_head
            root.right = root.left  # 注意这里连上的是左边linkedlist head --> root connected to left_linkedlist_head
            root.left = None

        return lastR or lastL or root
