class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        # 求有几块 不相似的words --> 相似的连成一块
        graph = collections.defaultdict(list)
        n = len(strs)

        # step1: build a graph for similar words connections --> {w1_index: similar_words_index}
        for i in range(n):
            for j in range(i + 1, n):
                w1 = strs[i]
                w2 = strs[j]
                if self.similar(w1, w2):
                    graph[i].append(j)
                    graph[j].append(i)

        # step2: for loop each words to see how many words not belongs to the same group --> num of islands
        visited = set()
        res = 0
        for i in range(n):
            if i not in visited:
                self.dfs(graph, visited, i)
                res += 1
        return res

    def similar(self, w1, w2):
        count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                count += 1
            if count > 2:
                return False
        return True

    def dfs(self, graph, visited, i):
        visited.add(i)

        for nei in graph[i]:
            if nei not in visited:
                self.dfs(graph, visited, nei)