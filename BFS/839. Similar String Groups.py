class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        # 求有几块 不相似的words --> 相似的连成一块
        graph = collections.defaultdict(list)
        n = len(strs)

        for i in range(n):
            for j in range(i + 1, n):
                w1 = strs[i]
                w2 = strs[j]
                if self.isSimilar(w1, w2):
                    graph[i].append(j)
                    graph[j].append(i)

        visited = set()
        res = 0
        for i in range(n):
            if i not in visited:
                self.bfs(graph, visited, i)
                res += 1
        return res

    def isSimilar(self, w1, w2):
        count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                count += 1
            if count > 2:
                return False
        return True

    def bfs(self, graph, visited, i):
        queue = collections.deque()
        queue.append(i)
        visited.add(i)

        while queue:
            cur = queue.popleft()
            for nei in graph[cur]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)