class Solution1:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = [[0] * 10 for _ in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5

        res = 0
        visited = [False] * 10
        for i in range(m, n + 1):
            res += self.dfs(1, i - 1, visited, skip) * 4
            res += self.dfs(2, i - 1, visited, skip) * 4
            res += self.dfs(5, i - 1, visited, skip)
        return res

    def dfs(self, i, remaining, visited, skip):
        if remaining < 0:
            return 0
        if remaining == 0:
            return 1
        visited[i] = True
        count = 0
        for j in range(1, 10):
            if not visited[j] and (skip[i][j] == 0 or visited[skip[i][j]]):
                count += self.dfs(j, remaining - 1, visited, skip)
        visited[i] = False
        return count


class Solution:
    # step1: 建图（save keys to be skipped)
    # step2: for loop each cur key and next key, if (curkey, nextkey) not in graph or graph[(curkey, nextkey)] is visited ---> nextkey is valid --> count ++
    def numberOfPatterns(self, m, n):
        tb_skipped = {(1, 3): 2, (4, 6): 5, (7, 9): 8,
                      (3, 1): 2, (6, 4): 5, (9, 7): 8,
                      (1, 7): 4, (2, 8): 5, (3, 9): 6,
                      (7, 1): 4, (8, 2): 5, (9, 3): 6,
                      (1, 9): 5, (3, 7): 5, (7, 3): 5, (9, 1): 5}
        self.res = 0
        for num in range(1, 10):
            visited = set()
            self.dfs(num, 1, m, n, visited, tb_skipped)
        return self.res

    def dfs(self, num, count, m, n, visited, tb_skipped):
        if m <= count <= n:
            self.res += 1

        if count == n:
            return
        visited.add(num)
        for nextNum in range(1, 10):
            if nextNum not in visited:
                if (num, nextNum) not in tb_skipped or tb_skipped[(num, nextNum)] in visited:
                    self.dfs(nextNum, count + 1, m, n, visited, tb_skipped)
        visited.remove(num)
