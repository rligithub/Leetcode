class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        # replace
        graph = collections.defaultdict(list)

        for u, v in synonyms:
            graph[u].append(v)
            graph[v].append(u)

        res = []

        visited = set()
        self.dfs(text, graph, text, res, visited)
        return sorted(res)

    def dfs(self, s, graph, path, res, visited):
        visited.add(path)
        res.append(path)

        words = path.split(" ")
        for i, word in enumerate(words):
            for nei in graph[word]:
                path = ' '.join(words[:i] + [nei] + words[i + 1:])
                if path not in visited:
                    self.dfs(s, graph, path, res, visited)
