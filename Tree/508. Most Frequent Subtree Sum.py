# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        # postorder每个左右node需要返回 subtree summ --> 不能用global variable
        self.maxx = 0
        hashmap = collections.defaultdict(int)
        self.dfs(root, hashmap)
        print(hashmap)
        res = []
        for num, cnt in hashmap.items():
            if cnt == self.maxx:
                res.append(num)

        return res

    def dfs(self, root, hashmap):
        if not root:
            return 0

        left = self.dfs(root.left, hashmap)
        right = self.dfs(root.right, hashmap)

        summ = left + right + root.val
        hashmap[summ] += 1
        self.maxx = max(self.maxx, hashmap[summ])
        return summ
