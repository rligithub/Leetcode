# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution2:  # super fast
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # BFS --> mark down with index
        queue = collections.deque()
        queue.append((root, 1))
        maxx = float('-inf')

        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                cur, idx = queue.popleft()
                if i == 0 or i == size - 1:
                    level.append(idx)

                if cur.left:
                    queue.append((cur.left, idx * 2))
                if cur.right:
                    queue.append((cur.right, idx * 2 + 1))

            maxx = max(maxx, level[-1] - level[0] + 1)
        return maxx


class Solution1:  # TLE
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # BFS --> append null Node with "#" --> skip if not level [] and level == "#" --> get max len(level)
        queue = collections.deque()
        queue.append(root)
        maxx = float('-inf')

        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                cur = queue.popleft()
                if not level and not cur:
                    continue
                if not cur:
                    level.append('#')
                else:
                    level.append(cur.val)

                if cur:
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    queue.append(None)
                    queue.append(None)
            for num in level[::-1]:
                if num == '#':
                    level.pop()
                else:
                    break

            maxx = max(maxx, len(level))
        return maxx


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS --> get index of each each node --> check same level
        self.res = 0
        table = {}
        self.dfs(root, 0, 0, table)
        return self.res

    def dfs(self, root, idx, depth, table):
        if not root:
            return

        if depth not in table:  # 记录每一层的第一个 index值
            table[depth] = idx

            # 每次比较该层的index值 与 第一个index值 --> 求最长长度
        self.res = max(self.res, idx - table[depth] + 1)

        self.dfs(root.left, idx * 2, depth + 1, table)
        self.dfs(root.right, idx * 2 + 1, depth + 1, table)






