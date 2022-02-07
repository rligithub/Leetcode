# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        dic1 = collections.defaultdict(int)
        dic2 = collections.defaultdict(int)
        self.dfs(root1, dic1)
        self.dfs(root2, dic2)

        return dic1 == dic2

    def dfs(self, root, counter):
        if root.val != '+':
            counter[root.val] += 1
        else:
            self.dfs(root.left, counter)
            self.dfs(root.right, counter)

        return counter

