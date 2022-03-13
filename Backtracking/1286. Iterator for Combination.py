class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        # combination
        self.res = []
        self.dfs(characters, combinationLength, 0, '')
        self.res = sorted(self.res)[::-1]

    def dfs(self, s, k, pos, path):

        if len(path) == k:
            self.res.append(path)
            return

        for i in range(pos, len(s)):
            self.dfs(s, k, i + 1, path + s[i])

    def next(self) -> str:
        return self.res.pop()

    def hasNext(self) -> bool:
        return self.res

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()