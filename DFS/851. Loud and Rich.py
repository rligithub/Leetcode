class Solution1:  # TLE
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # find richer and quietst person ---> 在所有拥有的钱肯定不少于 person x 的人中，person y 是最安静的人（也就是安静值 quiet[y] 最小的人）

        graph = collections.defaultdict(list)

        for u, v in richer:
            graph[v].append(u)  # {poor_person: richer people}
        n = len(quiet)
        self.res = []
        for i in range(n):
            self.ans = 0
            self.minn = float('inf')
            self.dfs(graph, quiet, i)
            self.res.append(self.ans)
        return self.res

    def dfs(self, graph, quiet, i):
        # find quiest person
        if quiet[i] < self.minn:
            self.minn = quiet[i]
            self.ans = i
        for nei in graph[i]:
            self.dfs(graph, quiet, nei)


class Solution:
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        graph = collections.defaultdict(list)
        for u, v in richer:
            graph[v].append(u)

        res = [0] * n
        for i in range(n):
            self.dfs(graph, i, quiet, res)
        return res

    def dfs(self, graph, i, quiet, res):
        # Want least quiet person in this subtree
        if res[i]:
            return res[i]
        res[i] = i
        for nei in graph[i]:
            pp = self.dfs(graph, nei, quiet, res)
            if quiet[pp] < quiet[res[i]]:
                res[i] = pp
        return res[i]
