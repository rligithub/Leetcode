"""
test
"""
import collections


class Solution:
    def findSongs(self, rideDuration, songDurations):

        # corner case
        if rideDuration < 30 or not songDurations or len(songDurations) < 2:
            return [-1, -1]

        # stop 30 seconds before rider reaches to their stop
        target = rideDuration - 30

        # find exact two songs --> two sum

        table = collections.defaultdict(list)
        for i, time in enumerate(songDurations):
            table[time].append(i)

        maxx = float('-inf')
        for i, time in enumerate(songDurations):
            if target - time in table:
                if maxx < max(time, target - time):
                    maxx = max(time, target - time)

        if maxx != float('-inf'):
            return sorted([table[max][0], table[target - maxx][0]])
        else:
            return [-1. -1]


import heapq
class Solution1:
    def bestCombo(popularity, k):


        num = math.ceil(math.log(k, 2))
        nums = [(abs(popularity[0]), popularity[0])]

        for node in popularity[1:]:
            # print(nums)
            if len(nums) < num:
                heapq.heappush(nums, (-abs(node), node))
            else:
                heapq.heappushpop(nums, (-abs(node), node))

        small = []
        while nums:
            node, val = heapq.heappop(nums)
            small.append(val)
        # print(nums)
        small_nums = subsets(small)
        small_nums.sort()
        summ = 0
        for num in popularity:
            if num >= 0:
                summ += num

        res = []
        for i in range(k):
            res.append(summ - small_nums[i])
        return res


    def subsets(nums):
        res = []
        dfs(nums, 0, 0, res)
        return res

    def dfs(nums, pos, summ, res):
        if pos == len(nums):
            res.append(summ)
            return res

        dfs(nums, pos + 1, summ + nums[pos], res)
        dfs(nums, pos + 1, summ, res)


a = Solution()
rideDuration = 90
songDurations = [11, 40, 40, 20, 12]
print(a.findSongs(rideDuration, songDurations))