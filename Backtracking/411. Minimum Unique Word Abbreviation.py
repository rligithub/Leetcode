class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:

        # step1: generate a sorted list with all possible abb. of target (sorted by length)
        res = []
        path = []
        self.dfs(target, 0, path, 0, res)
        string = sorted(res, key=len)

        # step2: exclude different size
        graph = []
        n = len(target)
        for word in dictionary:
            if len(word) == n:
                graph.append(word)
        if not graph:
            return str(n)

        # step3: check if it matched
        for abb in string:
            if all(not self.check(abb, d) for d in graph):
                return "".join(abb)
        return target

    def dfs(self, s, pos, path, count, res):
        if pos == len(s):
            res.append(path + [str(count)] if count else path)
            return

        self.dfs(s, pos + 1, path + ([str(count)] if count else []) + [s[pos]], 0, res)
        self.dfs(s, pos + 1, path, count + 1, res)

    def check(self, word1, word2):
        m, n = len(word1), len(word2)
        i = j = 0
        while True:
            if i == m and j == n:
                return True
            if i >= m or j >= n:
                return False
            if word1[i].isdigit():
                step = int(word1[i])
                i += 1
                j += step  # jump
            else:
                if word1[i] != word2[j]:
                    return False
                i += 1
                j += 1
        return True


