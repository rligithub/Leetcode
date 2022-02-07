class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # similar to #2097 一笔画问题
        graph = collections.defaultdict(list)

        for fr, to in tickets:
            graph[fr].append(to)

        path = []
        self.dfs(graph, 'JFK', path)
        return path[::-1]

    def dfs(self, graph, city, path):

        while graph[city]:
            nxtcity = (sorted(graph[city]))[0]
            graph[city].remove(nxtcity)
            self.dfs(graph, nxtcity, path)
        path.append(city)

