class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        if len(words) == 1:
            return words[0]

        # step1: build graph
        graph = collections.defaultdict(set)
        for word in words:
            for i in range(1, len(word)):
                prefix = word[:i]
                graph[prefix].add(word)

        # step2: for loop each start word, do dfs
        self.res = []
        for word in words:
            self.dfs(graph, word, 1, [word])

        return self.res

    def dfs(self, graph, word, pos, path):

        if pos == len(word):
            self.res.append(path[:])
            return
        prefix = ''
        for string in path:
            prefix += string[pos]

        if prefix in graph:
            for nextword in graph[prefix]:
                self.dfs(graph, word, pos + 1, path + [nextword])

class Solution:# tony
    def wordSquares(self, words):
        res = []
        table = collections.defaultdict(set)
        for word in words:
            for i in range(len(word)):
                table[word[:i]].add(word)
        for word in words:
            self.dfs(table, word, 1, [], res)
        return res

    def dfs(self, table, word, index, path, res):
        path.append(word)
        if index == len(word):
            res.append(path[:])
        else:
            prefix = "".join(path[i][index] for i in range(index))
            for word in table[prefix]:
                self.dfs(table, word, index + 1, path, res)
        path.pop()
