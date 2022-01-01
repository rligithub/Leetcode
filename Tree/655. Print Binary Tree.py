# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        # 先求树高 --> 然后BFS打印

        n = self.height(root)
        m = 2 ** n - 1
        res = [[""] * m for _ in range(n)]

        queue = collections.deque()
        queue.append((root, 0, 0, m))  # (root, i, l, r) --> root is in [i, (l+r)//2]

        while queue:
            node, i, l, r = queue.popleft()
            j = (l + r) // 2
            res[i][j] = str(node.val)

            if node.left:
                queue.append((node.left, i + 1, l, j))
            if node.right:
                queue.append((node.right, i + 1, j, r))

        return res

    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return max(left, right) + 1









