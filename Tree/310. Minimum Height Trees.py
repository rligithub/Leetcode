import collections
class Solution:
    def findMinHeightTrees(self, n, edges):
        # 打印最后一层的node path --> indegrees
        # prequsitions

        if n <= 1:
            return [0]

        neighbors = collections.defaultdict(list)
        indegrees = [0] * n

        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
            indegrees[u] += 1
            indegrees[v] += 1

        queue = collections.deque()
        for i in range(n):
            if indegrees[i] == 1:
                queue.append(i)

        # while queue:
        #     level = []
        #     res = queue
        #     for leaf in queue:
        #         for nei in neighbors[leaf]:
        #             indegrees[nei] -= 1
        #             if indegrees[nei] == 1:
        #                 level.append(nei)
        #     queue = level
        # return res

        visited = set()
        while queue:
            res = []
            size = len(queue)

            for i in range(size):
                cur = queue.popleft()
                visited.add(cur)
                res.append(cur)

                for nei in neighbors[cur]:
                    if nei not in visited:
                        indegrees[nei] -= 1
                        if indegrees[nei] == 1:
                            queue.append(nei)
        return res

a = Solution()
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
print(a.findMinHeightTrees(n, edges))