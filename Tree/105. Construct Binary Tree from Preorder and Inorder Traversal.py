'''
preorder : 3, 9, 20 15 7  --> root == 3 | root.left == 9 | root.right ==  20, 15, 7
inorder:   9, 3, 15 20 7  --> 15, 20, 7

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:  # fast
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder --> root + root.left + root.right
        # inorder --> root.left + root + root.right
        # find root index in inorder ---> root.left == index left side ; root.right == index right side

        if not preorder:
            return None

        return self.dfs(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)

    def dfs(self, preorder, inorder, preleft, preright, inleft, inright):

        if preleft > len(preorder) - 1 or inleft > inright:
            return None

        rootval = preorder[preleft]
        root = TreeNode(rootval)
        inIndex = inorder.index(rootval)

        root.left = self.dfs(preorder, inorder, preleft + 1, inIndex, inleft, inIndex - 1)
        root.right = self.dfs(preorder, inorder, preleft + inIndex + 1 - inleft, preright, inIndex + 1, inright)

        return root


class Solution2:  # slower
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        index = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[index])
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index + 1:])

        return root


class Solution:  # slowest
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])

        return root