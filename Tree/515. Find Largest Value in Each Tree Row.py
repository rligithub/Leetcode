# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        if not root:
            return []
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)
            maxx = float('-inf')
            for i in range(size):
                cur = queue.popleft()
                maxx = max(maxx, cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(maxx)

        return res


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # DFS
        self.res = []
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, level):
        if not root:
            return

            # 当每一层需要一个值的时候，比较res大小和level --> 更新较大值
        if level >= len(self.res):
            self.res.append(root.val)
        elif root.val > self.res[level]:
            self.res[level] = root.val

        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)