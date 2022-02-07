class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # 给n个花园种花，花的种类总共有4种 (1,2,3,4) ，要求相邻的花园种的种类不一样，返回其中一种种植方案

        graph = collections.defaultdict(list)
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)

        # 如果 花园都不相连 且 花园数大于 4 --> 指定color，每次color++ 则行不通 --> 必须要在dfs里for loop color 可重复
        flag = [0] * (n + 1)
        for i in range(1, n + 1):  # for loop flag --> garden
            self.dfs(graph, i, flag)
        return flag[1:]

    def dfs(self, graph, i, flag):
        color_used = set()
        for nei in graph[i]:
            if flag[nei] != 0:
                color_used.add(flag[nei])

        # 把该花 周围的颜色都存起来，把该花涂成不同的颜色
        for color in range(1, 5):
            if color not in color_used:
                flag[i] = color

