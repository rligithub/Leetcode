class Solution1:  # slow
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # 建一个播放清单，总共n首歌，要播放goal首歌，每播放不同的k首歌才能重播播放前面的歌， 求有几种方式建立播放清单
        # 每首歌都需要播放至少一次，可以重复播放
        # goal >= n
        # length + unique
        # TWO CASES: add new song or add repeat song
        memo = {}
        return self.dfs(n, goal, k, 0, 0, memo)

    def dfs(self, n, goal, k, count, unique, memo):
        if (count, unique) in memo:
            return memo[(count, unique)]

        if count == goal:
            if unique == n:
                return 1
            else:
                return 0

        mod = 10 ** 9 + 7

        # not_repeat songs --> add new song from the remaining songs (n - unique)
        add_new = self.dfs(n, goal, k, count + 1, unique + 1, memo) * (n - unique)

        # repeat songs --> add repeat song from the selected sings (unique - k) --> must meet k criterial
        add_repeat = self.dfs(n, goal, k, count + 1, unique, memo) * max(0, unique - k)

        memo[(count, unique)] = (add_new + add_repeat) % mod
        return memo[(count, unique)]


class Solution:  # super fast
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # 建一个播放清单，总共n首歌，要播放goal首歌，每播放不同的k首歌才能重播播放前面的歌， 求有几种方式建立播放清单
        # 每首歌都需要播放至少一次，可以重复播放
        # goal >= n
        # length + unique
        # TWO CASES: add new song or add repeat song
        memo = {}
        return self.dfs(n, goal, k, 0, 0, memo)

    def dfs(self, n, goal, k, count, unique, memo):
        if (count, unique) in memo:
            return memo[(count, unique)]

        if count == goal:
            if unique == n:
                return 1
            else:
                return 0

        mod = 10 ** 9 + 7

        add_new = self.dfs(n, goal, k, count + 1, unique + 1, memo) * (n - unique)

        add_repeat = 0
        if unique > k:
            add_repeat = self.dfs(n, goal, k, count + 1, unique, memo) * (unique - k)

        memo[(count, unique)] = (add_new + add_repeat) % mod
        return memo[(count, unique)]
