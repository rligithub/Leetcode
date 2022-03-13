class Solution1:
    def splitString(self, s: str) -> bool:
        # split 成 at least two 递减的数字，相邻数字相差为1 ，（可以有leading zero) --> return T/F

        path = []

        return self.dfs(s, path)

    def dfs(self, s, path):

        if len(path) >= 2 and path[-1] != path[-2] - 1:
            return False

        if not s and len(path) >= 2:
            return True

        for i in range(1, len(s) + 1):
            if self.dfs(s[i:], path + [int(s[:i])]):
                return True
        return False

