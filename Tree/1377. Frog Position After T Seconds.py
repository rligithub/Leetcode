class Solution1:
    def frogPosition(self, n, edges, t, target):
        if n == 1:
            return 1

        graph = collections.defaultdict(list)
        graph[1].append(1)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = collections.deque([(1, 0, 1, 2)])
        visited = set([1])

        while queue:
            node, time, prob, seen = queue.popleft()

            nei = 0  # Number of unvisited neighbors
            for adj in graph[node]:
                if (
                        1 << adj) & seen == 0:  # checks if adj has been visited, seen is just an integer to store visited nodes
                    nei += 1

            if node == target:
                if time == t or (time < t and nei == 0):
                    return prob
                else:
                    return 0

            prob_nei = 1 / nei if nei else 0

            for adj in graph[node]:
                if (1 << adj) & seen == 0:  # if neighbor is unvisited
                    queue.append([adj, time + 1, prob * prob_nei, seen ^ (1 << adj)])
        return 0


class Solution: # best
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([(1, 1.0)])
        depth = 0
        while queue:
            size = len(queue)
            for i in range(size):
                cur, prob = queue.popleft()
                if cur == target:
                    if depth == t:
                        return prob
                    if depth < t and not graph[cur]:
                        return prob
                    elif depth > t or graph[cur]:
                        return 0
                if graph[cur]:
                    for j in graph[cur]:
                        graph[j].remove(cur)  # visited
                        queue.append((j, prob / len(graph[cur])))
            depth += 1
        return 0


class Solution1:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.res = 0
        self.dfs(target, t, graph, 1, 1, 0)
        return self.res

    def dfs(self, target, t, graph, node, p, count):
        if node == target:
            if count == t or (count < t and not graph[node]):
                self.res = p
            else:
                self.res = 0

        if graph[node]:
            p = p * (1 / len(graph[node]))
            for nei in graph[node]:
                graph[nei].remove(node)
                self.dfs(target, t, graph, nei, p, count + 1)


class Solution2:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = collections.defaultdict(list)
        # fake parent for node 1
        graph[1].append(-1)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.res = 0
        self.dfs(1.0, 1, -1, graph, t, target)
        return self.res

    def dfs(self, prob, cur, parent, graph, t, target):
        # not enough t
        if t < 0:
            return

        # match target
        if cur == target:
            # no more t or no more child
            if t == 0 or len(graph[cur]) == 1:
                self.res = prob
            return

        # no child, return
        if len(graph[cur]) == 1:
            return

        # calculate new prob
        prob /= len(graph[cur]) - 1
        for child in graph[cur]:
            if child != parent:
                self.dfs(prob, child, cur, graph, t - 1, target)




