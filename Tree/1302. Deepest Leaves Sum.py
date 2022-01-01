# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # summ of deepest leaves --> BFS
        if not root:
            return 0
        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)
            res = 0
            for i in range(size):
                cur = queue.popleft()
                res += cur.val

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # summ of deepest leaves --> deepest leaf node sum
        self.hashmap = collections.defaultdict(list)
        self.dfs(root, 0)
        maxdepth = sorted(self.hashmap.keys())[-1]
        res = sum(self.hashmap[maxdepth])

        return res

    def dfs(self, root, depth):
        if not root:
            return

        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)

        if not root.left and not root.right:
            self.hashmap[depth].append(root.val)







