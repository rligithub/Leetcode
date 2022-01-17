
class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
        n = len(order)
        maxx = max(order)
        minn = min(order)

        if maxx == order[0] and minn == order[n - 1] or minn == order[0] and maxx == order[n - 1]:
            return n

        return self.dfs(order)

    def dfs(self, order): # slicing --> 缩小左右范围
        if len(order) <= 1:
            return 1

        root = order[0]
        left, right = [], []

        for i in order:
            if i > root:
                right.append(i)
            elif i < root:
                left.append(i)

        return 1 + max(self.dfs(left), self.dfs(right))



