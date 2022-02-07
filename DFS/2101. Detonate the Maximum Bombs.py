class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # 找最多能检测到几个bombs

        # for loop each start bombs ---> check how many bombs nearby --> check next bombs

        # step1: build graph --> add bombs can be seen by cur_bombs --> 不能用 坐标 作为key，如果有重复的坐标 没法count --> 用第几个点 来区别每个点
        graph = collections.defaultdict(list)
        n = len(bombs)  # num of bombs
        for i in range(n):
            for j in range(n):
                dist = (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2
                if dist <= bombs[i][2] ** 2:
                    graph[i].append(j)
        print(graph)

        res = 1
        for node in range(n):
            visited = set()
            self.dfs(graph, node, visited)
            res = max(res, len(visited))
        return res

    def dfs(self, graph, node, visited):
        visited.add(node)

        for nei in graph[node]:
            if nei not in visited:
                self.dfs(graph, nei, visited)

