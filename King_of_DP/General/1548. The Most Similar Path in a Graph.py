import collections


class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        # 给一个地图，a城市可以到b城市，求最相似的路径 （vs按照路线到每个目的地的路径）==> edit distance 最少差别

        graph = collections.defaultdict(list)

        for c1, c2 in roads:
            graph[c1].append(c2)
            graph[c2].append(c1)

        memo = {}
        res = float('inf')
        final_path = []
        for start_city in graph:
            dist, path = self.dfs(targetPath, names, graph, 0, start_city, memo)
            if dist < res:
                res = dist
                final_path = path
        return final_path

    def dfs(self, targetPath, names, graph, pos, city, memo):
        if (pos, city) in memo:
            return memo[(pos, city)]

        if pos >= len(targetPath):
            return [0, []]

        res = float('inf')
        final_path = []
        for nei in graph[city]:
            dist, path = self.dfs(targetPath, names, graph, pos + 1, nei, memo)

            if targetPath[pos] != names[city]:
                dist += 1
            if dist < res:
                res = dist
                final_path = [city] + path
        memo[(pos, city)] = [res, final_path]
        return memo[(pos, city)]





