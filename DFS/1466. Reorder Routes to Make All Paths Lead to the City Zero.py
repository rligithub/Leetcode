class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # 重新规划路线 --> how many nodes can't get to node zero
        # 反向想 ---> 从0遍历相邻的节点，加1， 如果方向相反， 不作为（用反向图前进）

        graph = collections.defaultdict(list)
        reverse = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            reverse[v].append(u)

        self.res = 0
        self.dfs(graph, reverse, 0)

        return self.res

    def dfs(self, graph, reverse, i):

        # 反向图前进 到下一个nodes
        for nei in reverse[i]:
            graph[nei].remove(i)
            self.dfs(graph, reverse, nei)

        # 从 0 出发到别的nodes，count ++
        for nei in graph[i]:
            self.res += 1
            reverse[nei].remove(i)
            self.dfs(graph, reverse, nei)
