class Solution1:  # slicing + print path
    def numTilePossibilities(self, tiles: str) -> int:
        # subset + permutation

        res = []
        path = ''
        tiles = sorted(list(tiles))
        tiles = ''.join(tiles)
        self.dfs(tiles, path, res)
        return len(res) - 1

    def dfs(self, s, path, res):

        res.append(path)

        visited = set()
        for i in range(len(s)):
            if s[i] in visited:
                continue
            visited.add(s[i])
            self.dfs(s[:i] + s[i + 1:], path + s[i], res)


class Solution:  # save index to set to replace slicing method
    def numTilePossibilities(self, tiles: str) -> int:
        # subset + permutation

        self.res = 0
        tiles = sorted(list(tiles))
        tiles = ''.join(tiles)
        self.dfs(tiles, set())
        return self.res - 1

    def dfs(self, s, used):

        self.res += 1

        visited = set()
        for i in range(len(s)):
            if s[i] in visited:
                continue
            if i in used:
                continue
            visited.add(s[i])
            used.add(i)
            self.dfs(s, used)
            used.remove(i)