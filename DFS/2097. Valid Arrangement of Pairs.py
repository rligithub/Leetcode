class Solution1:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # similar to leetcode 332 Reconstruct itinerary
        # 一笔画问题 --> 欧拉路径所有顶点要不入度出度相同；要不有一个点是起点，出度=入度+1；另外有一个点是终点，入度=出度+1。我们找到起点，dfs遍历并删边即可
        # for loop to find a path that can visit all nodes --> print out path

        # build graph
        indegree = collections.defaultdict(int)
        graph = collections.defaultdict(list)

        for u, v in pairs:
            graph[u].append(v)
            indegree[u] += 1
            indegree[v] -= 1

        start = pairs[0][0]  # set initial start node as first one in pairs
        for i in indegree:
            if indegree[i] == 1:  # find initial start node with indegree == 1
                start = i
                break
        self.res = []
        self.dfs(graph, start)
        return self.res[::-1]

    def dfs(self, graph, node):

        while graph[node]:
            nextnode = graph[node].pop()
            self.dfs(graph, nextnode)
            self.res.append([node, nextnode])


class Solution:  # TLE
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        indegree = collections.defaultdict(int)
        graph = collections.defaultdict(list)

        for u, v in pairs:
            graph[u].append(v)
            indegree[u] += 1
            indegree[v] -= 1

        # find start point
        start = pairs[0][0]
        for i in indegree:
            if indegree[i] == 1:
                start = i
                break

        path = []
        self.dfs(graph, start, path)  # path too long
        return path[::-1]

    def dfs(self, graph, node, path):

        while graph[node]:
            nxtnode = graph[node].pop()
            self.dfs(graph, nxtnode, path)
            path.append([node, nxtnode])
