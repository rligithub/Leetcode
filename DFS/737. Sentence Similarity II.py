class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        # 比较两个句子是否是相似的 --> for loop两个句子的每个词 dfs找 word1和word2是否是连接的
        if len(sentence1) != len(sentence2):
            return False

            # step1 --> build graph
        graph = collections.defaultdict(list)
        for u, v in similarPairs:
            graph[u].append(v)
            graph[v].append(u)

        # step2 --> for loop each word, compare sentence1[i] and sentence2[i] to see if they're connected

        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2:
                continue
            visited = set()
            if not self.dfs(graph, w1, w2, visited):
                return False
        return True

    def dfs(self, graph, w1, w2, visited):
        if w1 == w2:
            return True

        visited.add(w1)

        for nei in graph[w1]:
            if nei not in visited:
                if self.dfs(graph, nei, w2, visited):
                    return True


