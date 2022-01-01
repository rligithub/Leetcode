# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # record {value: count} --> find maxcount ---> get value
        self.count = collections.defaultdict(int)
        self.dfs(root)
        res = []
        maxcount = 1
        for num, cnt in self.count.items():
            if cnt > maxcount:
                maxcount = cnt
                res = [num]
            elif cnt == maxcount:
                res.append(num)

        return res

    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)
        self.count[root.val] += 1
        self.dfs(root.right)






