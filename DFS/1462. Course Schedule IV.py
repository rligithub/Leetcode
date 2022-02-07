class Solution:  # dfs + memo
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        # 求一串queries，问是否是prerequisite course

        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        res = [False] * len(queries)
        memo = {}
        for i, (course1, course2) in enumerate(queries):
            if self.dfs(graph, course1, course2, memo):
                res[i] = True

        return res

    def dfs(self, graph, c1, c2, memo):
        if (c1, c2) in memo:
            return memo[(c1, c2)]

        if c1 == c2:
            return True

        for nei in graph[c1]:
            if self.dfs(graph, nei, c2, memo):
                memo[(c1, c2)] = True
                return True
        memo[(c1, c2)] = False
        return False


