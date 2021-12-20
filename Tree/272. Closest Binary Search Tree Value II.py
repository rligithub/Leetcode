# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq


class Solution1:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # use heap
        heap = []
        self.dfs(root, heap, target, k)

        res = []
        for x in heap:
            res.append(x[1])
        return res

    def dfs(self, root, heap, target, k):
        if not root:
            return

        self.dfs(root.left, heap, target, k)
        heapq.heappush(heap, (- abs(root.val - target), root.val))
        if len(heap) > k:
            heapq.heappop(heap)
        self.dfs(root.right, heap, target, k)


class Solution:  # use inorder + sorted by abs(x-target)
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        res = self.dfs(root)

        res.sort(key=lambda x: abs(x - target))
        return res[:k]

    def dfs(self, root):
        if not root:
            return []

        return self.dfs(root.left) + [root.val] + self.dfs(root.right)