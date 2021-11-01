
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        # 青蛙跑田径绕开障碍物，每次可以往前跳一步，或者横着跳到不同lane， 请最少需要横着跳几次？
        # 如果前方有障碍， 只能横着跳 if cur_lane == obstacles[pos+1], 跳lane1, lane2, lane3. Need to make sure jump to different lane and the lane has no obstacles (lane != obstacles[pos])
        # 如果前方没障碍， 直接往前跳 if cur_lane != obstacles[pos+1]

        memo = {}
        return self.dfs(obstacles, 0, 2, memo)

    def dfs(self, obstacles, pos, cur_lane ,memo):
        if (pos, cur_lane) in memo:
            return memo[(pos, cur_lane)]

        if pos == len(obstacles) -1:
            return 0

        # if no obstacles in front, jump ahead
        if cur_lane != obstacles[pos + 1]:
            res = self.dfs(obstacles, pos + 1, cur_lane, memo)
        else:
            res = float('inf')
            for lane in range(1, 4):
                # 'lane to jump' has no obstacles, and must be in different lane
                if lane != obstacles[pos] and lane != cur_lane:
                    res = min(res, self.dfs(obstacles, pos + 1, lane, memo) + 1)

        memo[(pos, cur_lane)] = res
        return memo[(pos, cur_lane)]


class Solution1:
    def minSideJumps(self, obstacles: List[int]) -> int:

        memo = {}
        return self.dfs(obstacles, 0, 2, memo)

    def dfs(self, obstacles, pos, cur_lane, memo):
        if (pos, cur_lane) in memo:
            return memo[(pos, cur_lane)]

        if pos == len(obstacles):
            return 0

        if obstacles[pos] == cur_lane:
            return float('inf')

        # if no obstacles, jump ahead

        res = self.dfs(obstacles, pos + 1, cur_lane, memo)

        if pos < len(obstacles) - 1 and cur_lane == obstacles[pos + 1]:
            for lane in range(1, 4):
                if lane == obstacles[pos] or lane == cur_lane:
                    continue
                res = min(res, self.dfs(obstacles, pos + 1, lane, memo) + 1)

        memo[(pos, cur_lane)] = res
        return memo[(pos, cur_lane)]

