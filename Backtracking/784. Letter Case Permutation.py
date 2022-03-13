class Solution1:
    def letterCasePermutation(self, s: str) -> List[str]:
        # 对于每个char，可以换成 uppercase或者lowercase --> 相对顺序不变 --> 打印所有可能性

        res = []
        path = ''
        self.dfs(s, 0, path, res)
        return res

    def dfs(self, s, pos, path, res):

        if pos == len(s):
            res.append(path)
            return

        if s[pos].isalpha():
            self.dfs(s, pos + 1, path + s[pos].lower(), res)
            self.dfs(s, pos + 1, path + s[pos].upper(), res)
        else:
            self.dfs(s, pos + 1, path + s[pos], res)


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # 对于每个char，可以换成 uppercase或者lowercase --> 相对顺序不变 --> 打印所有可能性

        res = []
        path = ''
        self.dfs(s, 0, path, res)
        return res

    def dfs(self, s, pos, path, res):

        if pos == len(s):
            res.append(path)
            return

        # swap
        if s[pos].isalpha():
            self.dfs(s, pos + 1, path + s[pos].swapcase(), res)

        # not swap
        self.dfs(s, pos + 1, path + s[pos], res)
