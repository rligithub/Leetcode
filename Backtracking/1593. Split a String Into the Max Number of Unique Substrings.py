class Solution1:
    def maxUniqueSplit(self, s: str) -> int:
        visited = set()
        self.res = 0
        self.dfs(s, [], visited)
        return self.res

    def dfs(self, s, path, visited):

        if not s:
            self.res = max(self.res, len(path))
            return

        for i in range(1, len(s) + 1):
            if s[:i] in visited:
                continue
            visited.add(s[:i])
            self.dfs(s[i:], path + [s[:i]], visited)
            visited.remove(s[:i])  # backtracking


