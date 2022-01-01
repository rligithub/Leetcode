# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:  # serization + hashmap
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # serization + hashmap
        # subtree --> left, right, root --> val order
        # subtree --> str 'left, right, val'
        hashmap = collections.defaultdict(int)
        self.res = []
        self.dfs(root, hashmap)

        return self.res

    def dfs(self, root, hashmap):
        if not root:
            return '#'
        key = str(root.val) + ',' + self.dfs(root.left, hashmap) + ',' + self.dfs(root.right, hashmap)

        hashmap[key] += 1
        if hashmap[key] == 2:  # only need to append to res once
            self.res.append(root)
        return key


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode):
        self.table = collections.defaultdict(list)
        self.dfs(root)
        res = []
        for k in self.table:
            if len(self.table[k]) > 1:
                res.append(self.table[k][0])
        return res

    def dfs(self, root):
        if not root:
            return 'null'

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        subtree = str(root.val) + ',' + left + ',' + right
        self.table[subtree].append(root)
        return subtree


