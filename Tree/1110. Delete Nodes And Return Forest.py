# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # 删除给出的节点，返回每个subtree的root
        self.res = []
        to_delete = set(to_delete)

        node = self.dfs(root, to_delete)
        if node:
            self.res.append(node)
        return self.res

    def dfs(self, root, to_delete):
        if not root:
            return None

        root.left = self.dfs(root.left, to_delete)
        root.right = self.dfs(root.right, to_delete)

        if root.val in to_delete:
            to_delete.remove(root.val)
            if root.left:
                self.res.append(root.left)
            if root.right:
                self.res.append(root.right)
            return None

        return root