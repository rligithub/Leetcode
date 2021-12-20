# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS -> level order traversal --> level[::-1] by level
        # 注意：计算count的时候，必须在while loop外面，不然每次都会被reset
        if not root:
            return []

        res = []
        queue = collections.deque()
        queue.append(root)
        cnt = 0

        while queue:
            size = len(queue)
            cnt += 1
            level = []

            for i in range(size):
                cur = queue.popleft()
                level.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            if cnt % 2 == 0:
                level = level[::-1]
            res.append(level)

        return res 