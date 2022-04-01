class Solution:  # BFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # step1: build connections and indgerees
        neighbors = collections.defaultdict(list)
        indegree = collections.defaultdict(int)

        # create indegrees for every courses
        for course in range(numCourses):
            indegree[course] = 0

        # add indegrees and connections
        for u, v in prerequisites:
            neighbors[v].append(u)
            indegree[u] += 1

            # BFS --> initialization which indegree == 0
        queue = collections.deque()
        for i in indegree.keys():
            if indegree[i] == 0:
                queue.append(i)

        count = 0
        while queue:
            cur = queue.popleft()
            count += 1
            for nei in neighbors[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return count == numCourses



















