class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # 圆桌开会 每个人都有想一起坐的邻居， 问最多可以做几个人
        # TWO CASES: get max(case1, case2)
        # CASE1: circle > 2 --> can only allow for one circle --> get max circle
        # CASE2: circle <= 2 --> get max length

        # 使用label 记录当前环的编号，num记录当前环中的节点数目。
        # 如果碰见了环的入口，判断环中节点的数目。

        # step1: 构造反图 build graph --> {pp: people who like to seat next to this person}
        n = len(favorite)

        graph = collections.defaultdict(list)
        for i, pp in enumerate(favorite):
            graph[pp].append(i)

        path = [0] * n
        visited = [False] * n
        label = 1

        # step2: CASE1: find 最大环长 直接计算节点的数目
        maxcycle = 0
        for i in range(n):
            if path[i] == 0:
                maxcycle = max(maxcycle, self.findcycle(favorite, i, label, path, visited))

        # step3: CASE2: find 最大链长 根据反图求出两条链的最大长度和
        maxlen = 0
        for i in range(n):
            if favorite[favorite[i]] == i:  # if two people like to seat next to each other
                maxlen += self.finddepth(favorite, i, graph) + 1

        # step4: 答案是最大环长和链长中最大的一个
        res = max(maxcycle, maxlen)
        return res

    def findcycle(self, favorite, i, label, path, visited):

        visited[i] = True
        path[i] = label
        nxt = favorite[i]
        label += 1

        if not visited[nxt]:
            res = 0  # go forward --> no cirlce
        else:
            res = path[i] - path[nxt] + 1  # go back --> get circle size

        if path[nxt] == 0:
            res = max(res, self.findcycle(favorite, nxt, label, path, visited))
        visited[i] = False
        return res

    def finddepth(self, favorite, i, graph):
        res = 0
        for nxt in graph[i]:
            if favorite[i] != nxt:
                res = max(res, self.finddepth(favorite, nxt, graph) + 1)
        return res















