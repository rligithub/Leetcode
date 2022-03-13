class Solution1:  # slicing
    def expand(self, s: str) -> List[str]:
        res = []
        path = ''
        self.dfs(s, path, res)
        res = sorted(res)
        return res

    def dfs(self, s, path, res):

        if not s:
            res.append(path)
            return

        if s[0] == '{':
            index = s.find('}')
            for i in range(1, index):
                if not s[i].isalpha():
                    continue
                self.dfs(s[index + 1:], path + s[i], res)
        else:
            self.dfs(s[1:], path + s[0], res)


class Solution:  # indexing
    def expand(self, s: str) -> List[str]:
        res = []
        self.dfs(s, 0, "", res)
        res = sorted(res)
        return res

    def dfs(self, s, pos, path, res):

        if pos >= len(s):
            res.append(path)
            return

        if s[pos] == '{':
            end = s.find('}', pos)
            for i in range(pos + 1, end):
                if not s[i].isalpha():
                    continue
                self.dfs(s, end + 1, path + s[i], res)
        else:
            self.dfs(s, pos + 1, path + s[pos], res)