# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        # find distance of two nodes --> find a LCA of two nodes, use BFS to calculate dist between LCA and each nodes

        LCA = self.dfs(root, p, q)

        return self.dist(LCA, p) + self.dist(LCA, q)

    def dfs(self, root, p, q):
        if not root:
            return root

        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)

        if root.val == p or root.val == q:
            return root
        if left and right:
            return root
        if not left and not right:
            return None
        if left or right:
            return left or right

    def dist(self, root, a):
        if not root:
            return 0

        count = 0
        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)

            for i in range(size):
                cur = queue.popleft()
                if cur.val == a:
                    return count
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            count += 1


