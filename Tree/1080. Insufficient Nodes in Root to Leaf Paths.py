# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        # similar to #814 pruneTree --> 看subtree的左右孩子 node 有没有被included在pass_path里，都没有的话 返回none
        # pass_path --> return root
        # fail_path --> return None
        # if root.left or root.right --> root was used included in pass_path, otherwise, will be return None

        return self.dfs(root, limit)

    def dfs(self, root, limit):
        if not root:
            return None

        if not root.left and not root.right:
            if limit - root.val > 0:
                return None  # delete leaf nodes in fail_path
            else:
                return root

        root.left = self.dfs(root.left, limit - root.val)
        root.right = self.dfs(root.right, limit - root.val)

        if root.left or root.right:  # 只要有一个孩子存在 说明这个root被用在pass_path里
            return root
        else:
            return None  # 如果两个孩子都是fail_path，则这个root也是

