class Solution:  # TLE --> same as #95 pring out path --> get size of res
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        return len(self.dfs(1, n))

    def dfs(self, left, right):
        res = []
        if left > right:
            res.append(None)

        for k in range(left, right + 1):
            left_tree = self.dfs(left, k - 1)
            right_tree = self.dfs(k + 1, right)

            for l in left_tree:
                for r in right_tree:
                    root = TreeNode(k)
                    root.left = l
                    root.right = r
                    res.append(root)

        return res


class Solution:  # dp
    '''
    n: childnodes
    1: f(0) = 1
    2: f(0)*f(1) + f(1)*f(0) = 1*1+1*1 = 2
    3: f(0)*f(2) + f(1)*f(1) + f(2)*f(0) = 1*2+1*1+2*1 = 5
    4: f(0)*f(3) + f(1)*f(2) + f(2)*f(1) + f(3)*f(0) = 1*5+1*2+2*1+5*1=14
    n: f(0)*f(n-1) + f(1)*f(n-2) +...f(n-1)*f(0)


    '''

    def numTrees(self, n: int) -> int:
        memo = {}
        return self.dfs(n, memo)

    def dfs(self, n, memo):
        if n in memo:
            return memo[n]

        if n == 0 or n == 1:
            return 1

        res = 0
        for i in range(n):
            left = self.dfs(i, memo)
            right = self.dfs(n - i - 1, memo)
            res += left * right

        memo[n] = res
        return res 