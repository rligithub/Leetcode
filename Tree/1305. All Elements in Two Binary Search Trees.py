# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res1 = []
        res2 = []
        res = []

        self.dfs(root1, res1)
        self.dfs(root2, res2)

        i, j = 0, 0
        while i < len(res1) and j < len(res2):
            if res1[i] <= res2[j]:
                res.append(res1[i])
                i += 1
            else:
                res.append(res2[j])
                j += 1
        while i < len(res1):
            res.append(res1[i])
            i += 1
        while j < len(res2):
            res.append(res2[j])
            j += 1
        return res

    def dfs(self, root, res):
        if not root:
            return

        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)
