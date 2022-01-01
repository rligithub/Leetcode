# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # preorder --> ROOT + LEFT + RIGHT
        # postorder --> LEFT + RIGHT + ROOT
        if not preorder:
            return None

        n = len(preorder)
        return self.dfs(preorder, postorder, 0, n - 1, 0, n - 1)

    def dfs(self, preorder, postorder, a, b, x, y):
        if a > b:
            return None
        if a == b:
            return TreeNode(preorder[a])

        root = TreeNode(preorder[a])
        idx = postorder.index(preorder[a + 1])
        size = idx - x + 1
        root.left = self.dfs(preorder, postorder, a + 1, a + size, x, idx)
        root.right = self.dfs(preorder, postorder, a + size + 1, b, idx + 1, y - 1)

        return root


class Solution1:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:

        def search(preorder, a, b, x, y):
            if a > b:
                return None
            if a == b:
                return TreeNode(preorder[a])

            root = TreeNode(preorder[a])

            index_post = postorder.index(preorder[a + 1])
            root.left = search(preorder, a + 1, index_post - x + a + 1, x, index_post)
            root.right = search(preorder, index_post - x + a + 2, b, index_post + 1, y - 1)

            return root

        return search(preorder, 0, len(preorder) - 1, 0, len(postorder) - 1)


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:

        if not pre:
            return None
        node = TreeNode(pre[0])

        if len(pre) == 1:
            return node

        idx = post.index(pre[1])

        node.left = self.constructFromPrePost(pre[1:idx + 2], post[:idx + 1])
        node.right = self.constructFromPrePost(pre[idx + 2:], post[idx + 1:-1])
        return node

