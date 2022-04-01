class Solution:  # BFS
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        neighbors = collections.defaultdict(list)
        indegree = collections.defaultdict(int)

        for course in range(numCourses):
            indegree[course] = 0

        for u, v in prerequisites:
            neighbors[v].append(u)
            indegree[u] += 1

        path = []
        queue = collections.deque()
        for i in indegree.keys():
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            cur = queue.popleft()
            path.append(cur)

            for nei in neighbors[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        if len(path) == numCourses:
            return path
        return []