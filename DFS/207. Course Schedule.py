import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # check if there is cycle for each nodes
        neighbors = collections.defaultdict(list)

        for u, v in prerequisites:
            neighbors[v].append(u)

        flag = [0] * numCourses
        for i in range(numCourses):
            if not self.dfs(neighbors, i, flag):
                return False
        return True

    def dfs(self, neighbors, i, flag):
        if flag[i] == -1:  # visited --> check has cycle
            return False
        if flag[i] == 1:  # backtrack --> finished check --> no cycle
            return True

        flag[i] = -1

        for nei in neighbors[i]:
            if not self.dfs(neighbors, nei, flag):
                return False
        flag[i] = 1  # backtracking --> no cycle
        return True

