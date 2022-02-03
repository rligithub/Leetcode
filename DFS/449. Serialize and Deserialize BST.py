# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        # preoder
        self.res = []
        self.dfs1(root)

        return ' '.join(self.res)

    def dfs1(self, root):
        if not root:
            return ''
        self.res.append(str(root.val))
        self.dfs1(root.left)
        self.dfs1(root.right)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        data = data.split()
        self.pos = 0
        res = self.dfs(data, float('-inf'), float('inf'))
        return res

    def dfs(self, data, minn, maxx):
        if self.pos == len(data):
            return None

        val = int(data[self.pos])

        if val < minn or val > maxx:
            return None
        self.pos += 1
        root = TreeNode(val)
        root.left = self.dfs(data, minn, val)
        root.right = self.dfs(data, val, maxx)
        return root

    # Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans