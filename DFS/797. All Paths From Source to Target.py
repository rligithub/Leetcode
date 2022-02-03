class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # print all path --> combination
        path = []
        res = []

        self.dfs(graph, 0, path, len(graph), res)
        return res

    def dfs(self, graph, i, path, n, res):
        if i == n - 1:
            path.append(i)
            res.append(path)

        for nei in graph[i]:
            self.dfs(graph, nei, path + [i], n, res)

