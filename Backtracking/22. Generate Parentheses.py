class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 打印出所有合法的 n个左右括号 的组合
        res = []
        path = []
        self.dfs(n, 0, 0, path, res)
        return res

    def dfs(self, n, left, right, path, res):
        if right > left:
            return

        if left > n or right > n:
            return

        if len(path) == 2 * n:
            res.append(''.join(path))
            return

        self.dfs(n, left + 1, right, path + ['('], res)
        self.dfs(n, left, right + 1, path + [')'], res)


class Solution: # backtracking
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        self.dfs(n, 0, 0, path, res)
        return res

    def dfs(self, n, left, right, path, res):
        if right > left:
            return

        if left > n or right > n:
            return

        if len(path) == 2 * n:
            res.append(''.join(path))
            return

        path.append('(')
        self.dfs(n, left + 1, right, path, res)
        path.pop()

        path.append(')')
        self.dfs(n, left, right + 1, path, res)
        path.pop()