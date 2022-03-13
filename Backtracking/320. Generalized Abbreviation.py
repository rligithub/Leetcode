class Solution1:  # pos
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        path = ''
        self.dfs(word, 0, "", res)
        return res

    def dfs(self, word, pos, path, res):
        if pos == len(word):
            res.append(path)
            return

        # CASE1: not change to digits - use char
        self.dfs(word, pos + 1, path + word[pos], res)

        # CASE2: change to digits
        if not path or path[-1].isalpha():  # 数字和数字间要隔一个char --> 检查上一步是不是char
            for i in range(pos + 1, len(word) + 1):
                self.dfs(word, i, path + str(i - pos), res)


class Solution:  # no pos , slicing
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []

        self.dfs(word, "", res)
        return res

    def dfs(self, word, path, res):
        if not word:
            res.append(path)
            return

        # CASE1: not change to digits - use char
        self.dfs(word[1:], path + word[0], res)

        # CASE2: change to digits
        if not path or path[-1].isalpha():  # 数字和数字间要隔一个char --> 检查上一步是不是char
            for i in range(1, len(word) + 1):
                self.dfs(word[i:], path + str(i), res)

