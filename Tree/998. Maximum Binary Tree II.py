# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # insert node, if root.val > target --> insert it in child node which has None value or smaller value than target
        return self.dfs(root, val)

    def dfs(self, root, val):
        if root and root.val > val:
            root.right = self.dfs(root.right, val)
            return root

        node = TreeNode(val)
        node.left = root
        return node


class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 在#654的基础上，在array后面append一个新的val。
        # 654 是找个最大值作为root，最大值左边的数作为left subtree，最大值右边的数作为right subtree。如果在最后面append一个数且val不是最大值，则val铁定是右孩子
        return self.dfs(root, val)

    def dfs(self, root, val):
        if not root or root.val < val:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        elif root.val > val:
            root.right = self.dfs(root.right, val)
            return root

        return None





