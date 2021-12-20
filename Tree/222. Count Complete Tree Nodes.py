# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # BFS --> count # of nodes
        if not root:
            return 0

        res = 0
        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)

            level = 0
            for i in range(size):
                cur = queue.popleft()
                level += 1

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            res += level
        return res
