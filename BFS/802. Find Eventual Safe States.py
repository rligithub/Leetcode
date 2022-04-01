class Solution:  # super fast
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # similar to course schedule --> to find circle --> use topologic sort (indegree)
        # note that there is outdegree --> so reverse the relationship in the graph
        outdegree = collections.defaultdict(int)
        reverse = collections.defaultdict(list)

        for i in range(len(graph)):
            outdegree[i] = len(graph[i])
            for j in graph[i]:
                reverse[j].append(i)

        queue = collections.deque()
        visited = set()
        for i in outdegree.keys():
            if outdegree[i] == 0:
                queue.append(i)
                visited.add(i)

        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)

            for nei in reverse[cur]:
                outdegree[nei] -= 1
                if nei not in visited and outdegree[nei] == 0:
                    queue.append(nei)
                    visited.add(nei)

        return sorted(res)


