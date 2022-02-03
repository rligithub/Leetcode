class Solution1:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # similar to #210 course schedule II ---> res order is different --> course schedule II need to print ordering of course we should take
        # step1 --> build flag
        # step2 --> for loop flag, print out
        res = []
        flag = [0] * len(graph)
        for i in range(len(graph)):
            if flag[i] == 0:
                self.dfs(graph, i, flag)

        for i in range(len(graph)):
            if flag[i] == 1:
                res.append(i)

        return res

    def dfs(self, graph, i, flag):
        if flag[i] == -1:  # visited --> check has cycle
            return False
        if flag[i] == 1:  # backtrack --> finished check --> no cycle
            return True

        flag[i] = -1

        for nei in graph[i]:
            if not self.dfs(graph, nei, flag):
                return False
        flag[i] = 1  # backtracking --> no cycle

        return True


class Solution:  # super fast
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # check if there is no circle? if no circle --> print
        res = []
        flag = [0] * len(graph)
        for i in range(len(graph)):
            if self.dfs(graph, i, flag):
                res.append(i)

        return res

    def dfs(self, graph, i, flag):
        if flag[i] == -1:  # visited --> check has cycle
            return False
        if flag[i] == 1:  # backtrack --> finished check --> no cycle
            return True

        flag[i] = -1

        for nei in graph[i]:
            if not self.dfs(graph, nei, flag):
                return False
        flag[i] = 1  # backtracking --> no cycle

        return True