class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # how many connected provinces

        # step1: build graph
        graph = collections.defaultdict(list)

        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    graph[i].append(j)

        # step2: count
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                self.dfs(graph, i, visited)
                count += 1
        return count

    def dfs(self, graph, i, visited):
        visited.add(i)

        for nei in graph[i]:
            if nei not in visited:
                self.dfs(graph, nei, visited)