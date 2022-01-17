import collections
import math
class Solution:# TLE
    def getCoprimes(self, nums, edges):
        # 求每个index 最近的parent index 且 nums[index] 和 nums[parent_index] 互为质数
        # return res
        graph = collections.defaultdict(list)  # undirect graph --> need to find which one is parent
        parents = collections.defaultdict(list)  # {child: parent, parent_parent, ppp...}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = collections.deque()
        queue.append(0)
        visited = set()
        visited.add(0)

        while queue:
            cur = queue.popleft()
            for nei in graph[cur]:
                if nei not in visited:
                    parents[nei].append(cur)
                    if cur in parents:
                        parents[nei] += parents[cur]
                    queue.append(nei)
                    visited.add(nei)

        n = len(nums)
        res = [-1] * n

        for i in range(n):
            for p in parents[i]:
                if math.gcd(nums[i], nums[p]) == 1:
                    res[i] = p
                    break
        return res


a = Solution()
nums = [9,16,30,23,33,35,9,47,39,46,16,38,5,49,21,44,17,1,6,37,49,15,23,46,38,9,27,3,24,1,14,17,12,23,43,38,12,4,8,17,11,18,26,22,49,14,9]
edges = [[17,0],[30,17],[41,30],[10,30],[13,10],[7,13],[6,7],[45,10],[2,10],[14,2],[40,14],[28,40],[29,40],[8,29],[15,29],[26,15],[23,40],[19,23],[34,19],[18,23],[42,18],[5,42],[32,5],[16,32],[35,14],[25,35],[43,25],[3,43],[36,25],[38,36],[27,38],[24,36],[31,24],[11,31],[39,24],[12,39],[20,12],[22,12],[21,39],[1,21],[33,1],[37,1],[44,37],[9,44],[46,2],[4,46]]

print(a.getCoprimes(nums, edges))