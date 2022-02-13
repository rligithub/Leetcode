class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # similar to course schedule --> need to check if there is circle and if last node == target
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        flag = [0] * n
        return self.dfs(graph, flag, source, destination)

    def dfs(self, graph, flag, start, end):
        if flag[start] == -1:  # checked circle
            return False
        if flag[start] == 1:  # checked no circle
            return True
        if len(graph[start]) == 0:  # check if last node == target
            return start == end

        flag[start] = -1

        for nei in graph[start]:
            if not self.dfs(graph, flag, nei, end):
                return False

        flag[start] = 1
        return True


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # move base case after dfs
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        flag = [0] * n
        return self.dfs(graph, flag, source, destination)

    def dfs(self, graph, flag, start, end):
        if flag[start] == -1:  # checked circle
            return False
        if flag[start] == 1:  # checked no circle
            return True

        flag[start] = -1

        for nei in graph[start]:
            if not self.dfs(graph, flag, nei, end):
                return False

        flag[start] = 1
        if len(graph[start]) == 0:  # check if last node == target
            return start == end

        return True
