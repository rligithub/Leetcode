# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.visited = set()
        self.dfs(root, 0)

    def dfs(self, root, val):
        if not root:
            return
        root.val = val
        self.visited.add(val)
        self.dfs(root.left, val * 2 + 1)
        self.dfs(root.right, val * 2 + 2)

    def find(self, target: int) -> bool:
        if target in self.visited:
            return True
        else:
            return False

        # Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)