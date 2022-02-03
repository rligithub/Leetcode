class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = collections.defaultdict(dict)

        for val, (num1, num2) in zip(values, equations):
            graph[num1][num2] = val
            graph[num2][num1] = 1 / val

        res = []
        for X, Y in queries:
            visited = set()
            res.append(self.dfs(X, Y, visited, graph))
        return res

    def dfs(self, a, b, visited, graph):
        if a not in graph: # or b not in graph
            return -1
        if a == b and a in graph:
            return 1

        for k in graph[a]:
            if k in visited:
                continue
            visited.add(k)
            res = self.dfs(k, b, visited, graph)
            if res != -1:
                return res * graph[a][k]
        return -1


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = collections.defaultdict(dict)

        for val, (num1, num2) in zip(values, equations):
            graph[num1][num2] = val
            graph[num2][num1] = 1 / val

        res = []
        for X, Y in queries:
            if X not in graph: # or Y not in graph
                res.append(-1)
            else:
                res.append(self.dfs(X, Y, set(), 1, graph))
        return res

    def dfs(self, a, b, visited, val, graph):
        if a == b:
            return val

        visited.add(a)
        for k in graph[a]:
            if k not in visited:
                res = self.dfs(k, b, visited, val * graph[a][k], graph)
                if res != -1:
                    return res
        return -1

