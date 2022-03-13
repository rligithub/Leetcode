class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = []
        res.append(start)

        visited = set()
        visited.add(start)

        self.dfs(n, visited, start, res)
        return res

    def dfs(self, n, visited, code, res):

        if len(res) == 1 << n:
            return True

        for i in range(n):
            new_code = code ^ (1 << i)
            if new_code in visited:
                continue
            visited.add(new_code)
            res.append(new_code)
            if self.dfs(n, visited, new_code, res):
                return True
            visited.remove(new_code)
            res.pop()

        return False
