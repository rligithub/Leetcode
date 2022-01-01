# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        # 4 ( 2(3)(1) )  ( 6(5) ) --> find '(', idx ++ ; find ')', idx -- ===> when idx == 0 get对应的左右括号
        # root + '(' + left node + ')' + '(' + right node +')'
        # recursive --> i = 第一个左括号index ； j = 对应的右括号index
        i = s.find('(')
        if i < 0: # if not find ---> return -1
            return TreeNode(int(s)) if s else None

        count = 0
        for j, char in enumerate(s):
            if char == '(':
                count += 1
            if char == ')':
                count -= 1
            if j > i and count == 0:
                break

        root = TreeNode(int(s[:i]))
        root.left = self.str2tree(s[i + 1: j])
        root.right = self.str2tree(s[j + 2: -1])
        return root

class Solution1:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        def dfs(s, idx):
            start = idx
            while idx < len(s) and (s[idx] == '-' or s[idx].isdigit()):
                idx += 1
            root = TreeNode(int(s[start: idx]))
            if idx < len(s) and s[idx] == '(':
                root.left, idx = dfs(s, idx+1)
            if idx < len(s) and s[idx] == '(':
                root.right, idx = dfs(s, idx+1)
            return root, idx+1

        if not s:
            return None
        root, _ = dfs(s, 0)
        return root