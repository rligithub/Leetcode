class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # combination --> each time fill num 1 or num 2... n
        # two case:
        # 1) num == 1: only need to fill once --> path[pos]
        # 2) num > 1: need tp fill in two position --> path[pos] and path[pos + num]

        path = [0] * (2 * n - 1)

        res = []
        self.dfs(n, 0, set(), path, res)
        return path

    def dfs(self, n, pos, visited, path, res):

        if len(visited) == n:
            return True

        for num in range(n, 0, -1):  # 从大到小试 ---> 排序
            while pos < len(path) and path[pos] != 0:
                pos += 1

            if num == 1 and num not in visited:
                visited.add(num)
                path[pos] = num
                if self.dfs(n, pos + 1, visited, path, res):
                    return True
                path[pos] = 0
                visited.remove(num)
            if num not in visited and pos + num < len(path) and path[pos] == 0 and path[pos + num] == 0:
                path[pos] = num
                path[pos + num] = num
                visited.add(num)
                if self.dfs(n, pos + 1, visited, path, res):
                    return True
                visited.remove(num)
                path[pos] = 0
                path[pos + num] = 0

