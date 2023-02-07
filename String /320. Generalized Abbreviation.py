
class Solution:  # pos
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        path = ""
        self.dfs(word, 0, path, res)
        return res

    def dfs(self, word, pos, path, res):
        if pos == len(word):
            res.append(path)
            return

            # not convert to num
        self.dfs(word, pos + 1, path + word[pos], res)

        # convert to num --> need to check if prev is alpha
        if not path or path[-1].isalpha():
            for i in range(pos, len(word)):
                self.dfs(word, i + 1, path + str(i - pos + 1), res)






