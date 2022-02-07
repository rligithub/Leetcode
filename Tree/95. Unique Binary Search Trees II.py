
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []

        return self.dfs(1, n)

    def dfs(self, start, end):
        res = []

        # stop points --> 左边的值大于右边的值就不符合条件
        if start > end:
            res.append(None)

        for k in range(start, end + 1):  # 枚举可行根节点
            # 获得所有可行的左子树集合
            leftTrees = self.dfs(start, k - 1)
            # 获得所有可行的右子树集合
            rightTrees = self.dfs(k + 1, end)

            # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
            for l in leftTrees:
                for r in rightTrees:
                    root = TreeNode(k)
                    root.left = l
                    root.right = r
                    res.append(root)

        return res

n = 3
a = Solution()
print(a.generateTrees(n))