class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # for loop each node --> 把连在一起的点放到visited里 --> 如果不在visited里，就count ++
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = collections.deque()
        visited = set()

        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                queue.append(i)
                visited.add(i)
                while queue:
                    cur = queue.popleft()
                    for nei in graph[cur]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)

        return count