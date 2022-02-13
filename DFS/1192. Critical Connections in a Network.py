class Solution1:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # 找环出现的位置 --> 环肯定是critical的
        # not return res in dfs --> slower

        graph = collections.defaultdict(list)

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        res = []
        rank = [None] * n
        self.dfs(graph, -1, 0, 1, rank, res)

        return res

    def dfs(self, graph, parent, i, label, rank, res):
        if rank[i]:
            return

        rank[i] = label

        for nei in graph[i]:
            if nei == parent:
                continue
            self.dfs(graph, i, nei, label + 1, rank, res)
            if rank[nei] == label + 1:
                res.append([i, nei])
            else:
                rank[i] = min(rank[i], rank[nei])


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # 找环出现的位置 --> 环肯定是critical的
        # return res in dfs ---> faster
        graph = collections.defaultdict(list)

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        res = []
        rank = [None] * n
        return self.dfs(graph, -1, 0, 1, rank, res)

    def dfs(self, graph, parent, i, label, rank, res):
        # 如果已经标记过了 直接返回标记的数
        if rank[i]:
            return
            # 每次标记一下 数
        rank[i] = label
        for nei in graph[i]:
            if nei == parent:
                continue
            self.dfs(graph, i, nei, label + 1, rank, res)

            # 如果下一个标记的数字比当前的应该要标记的数字 小，说明有cycle 走回去了 --> back tracking 把数字给成小的数 ---> 如果下一个标记的数字比当前的数字要大，说明 没有环，可以打印
            if rank[nei] != label + 1:
                rank[i] = min(rank[i], rank[nei])
            else:
                res.append([i, nei])

        return res

