class Solution2:  # not success
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        # 旅行到一个目的地，整点才能出发到下一个，如果不整点出发，最少需要skip几次休息能保证准点到达
        # skip vs not_skip 比较
        # skip ====> 判断 是不是整点 --> 整点； 不整点 + 1
        # not_skip ===> cur_dist //speed + 1

        if sum(dist) // speed > hoursBefore:
            return -1
        memo = {}
        return self.dfs(dist, speed, hoursBefore, 0, 0, memo)

    def dfs(self, dist, speed, hoursBefore, pos, accum_hrs, memo):
        if (pos, accum_hrs) in memo:
            return memo[(pos, accum_hrs)]

        if pos == len(dist):
            return 0

        if accum_hrs > hoursBefore:
            return float('inf')

        res = float('inf')
        if accum_hrs + (dist[pos] / speed) <= hoursBefore:
            # 整点 -> skip 和 not_skip是一样的
            if dist[pos] % speed == 0:

                total_hrs = accum_hrs + dist[pos] // speed
                res = self.dfs(dist, speed, hoursBefore, pos + 1, total_hrs, memo)
            else:
                # 不整点
                hrs_not_skipped = accum_hrs + dist[pos] // speed + 1
                not_skip = self.dfs(dist, speed, hoursBefore, pos + 1, hrs_not_skipped, memo)

                hrs_skipped = accum_hrs + dist[pos] // speed
                skip = self.dfs(dist, speed, hoursBefore, pos + 1, hrs_skipped, memo) + 1

            res = min(skip, not_skip)

        memo[(pos, accum_hrs)] = res
        return memo[(pos, accum_hrs)]


class Solution:
    def minSkips(self, dist, speed: int, hoursBefore: int) -> int:
        memo = {}
        for k in range(len(dist)):
            if self.dfs(dist, speed, 0, k, memo) <= hoursBefore:
                return k
        return -1

    def dfs(self, dist, speed, i, k, memo):
        if (i, k) in memo:
            return memo[(i, k)]

        if k < 0:
            return float('inf')

        if i >= len(dist):
            return 0

        skip = self.dfs(dist, speed, i + 1, k - 1, memo) + dist[i] / speed
        no_skip = math.ceil(self.dfs(dist, speed, i + 1, k, memo) + dist[i] / speed - 1e-9)

        memo[(i, k)] = min(skip, no_skip)
        return memo[(i, k)]

