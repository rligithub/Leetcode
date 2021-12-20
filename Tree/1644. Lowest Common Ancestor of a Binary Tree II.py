class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # similar to #236 but the p or q may not be exist
        self.count = 0
        res = self.dfs(root, p, q)
        print(self.count)
        if self.count == 2:
            return res
        else:
            return None

    def dfs(self, root, p, q):
        if not root:
            return root

        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)

        # check p and q here --> after recurisive, otherwise, it will return early
        if root == p or root == q:
            self.count += 1
            return root

        if left and right:
            return root
        if not left and not right:
            return None
        if left or right:
            return left or right
