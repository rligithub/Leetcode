# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS - level order traversal --> bottom to up
        # 注意检查 corner case!!!!!
        if not root:
            return []

        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)
            level = []

            for i in range(size):
                cur = queue.popleft()
                level.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            res.append(level)

        return res[::-1]
