class Solution1:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        zeros = []  # 记录晴天的日期
        lakes = {}  # 记录每个湖泊下雨的日期
        res = [1] * len(rains)  # 初始化 把所有没有用到的0置为任意正数

        for i, water in enumerate(rains):
            if water == 0:
                zeros.append(i)
                continue

            if water in lakes:
                pos = bisect.bisect_left(zeros, lakes[water])  # 查找上次下雨后 能找到第一个晴天日期
                if pos == len(zeros):  # 找不到就不可避免的洪水了
                    return []
                res[zeros[pos]] = water  # 如果找到了，就可以使用那一天抽水 -->抵消 上次下雨 和 dry --> 更新到这次下雨的日期
                zeros.pop(pos)

            lakes[water] = i
            res[i] = -1

        return res


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = [1] * len(rains)
        lakes = {}
        zeros = []

        for i, water in enumerate(rains):
            if water == 0:
                zeros.append(i)
                continue

            if water in lakes:
                pos = self.findFirstPosition(zeros, lakes[water])
                if pos == len(zeros):  # no zero after last rain
                    return []
                res[zeros[pos]] = water
                zeros.pop(pos)
            lakes[water] = i
            res[i] = -1

        return res

    def findFirstPosition(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

































