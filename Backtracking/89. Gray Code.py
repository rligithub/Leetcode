class Solution1:
    def grayCode(self, n: int) -> List[int]:

        res = []
        res.append(0)

        visited = set()
        visited.add(0)

        self.dfs(n, visited, 0, res)
        return res

    def dfs(self, n, visited, code, res):

        if len(res) == 1 << n:
            return True

        mask = 1
        for i in range(n):
            new_code = code ^ (mask << i)
            if new_code in visited:
                continue
            visited.add(new_code)
            res.append(new_code)
            if self.dfs(n, visited, new_code, res):
                return True
            visited.remove(new_code)
            res.pop()

        return False


class Solution: #TLE
    def grayCode(self, n: int) -> List[int]:

        res = []
        path = []
        path.append(0)
        visited = set()
        visited.add(0)

        self.dfs(n, visited, 0, path, res)
        return res[0]

    def dfs(self, n, visited, code, path, res):

        if len(path) == 1 << n:
            res.append(path[:])
            return

        for i in range(n):
            new_code = code ^ (1 << i)
            if new_code in visited:
                continue
            visited.add(new_code)
            self.dfs(n, visited, new_code, path + [new_code], res)
            if res:
                return
            visited.remove(new_code)


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        for i in range(1 << n):
            res.append(i ^ (i >> 1))
        return res