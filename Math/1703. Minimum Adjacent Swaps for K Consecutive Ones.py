class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        # 先构造一个新数组p，里面的元素就是原数组中所有1的位置
        p = []
        for i in range(len(nums)):
            if nums[i] == 1:
                p.append(i)

        # 在数组p中考察所有长度为k的滑窗
        # find first k
        summ = 0
        for i in range(k):
            summ += abs(p[i] - p[k // 2])

        res = summ

        # sliding window for size k --> find middle point as origin, get distance
        # 1 - 3, 2 - 3, 3 - 3, 4 - 3, 5 - 3
        #        2 - 4, 3 - 4, 4 - 4, 5 - 4, 6 - 4
        # minue p[0] - p[mid]
        # add p[mid] - p[mid+1] for num before mid
        # add p[k] - p[mid+1]
        # minue p[mid] - p[mid+1] for num after mid

        for i in range(len(p) - k):
            mid = i + k // 2
            summ -= abs(p[i] - p[mid])  # minus dist p[0] --> between old left and mid
            summ += abs(p[mid + 1] - p[mid]) * (k // 2)  # 每个数到新中心都多出了p[mid+1]-p[mid]
            summ += abs(p[i + k] - p[mid + 1])  # add dist between right and mid
            summ -= abs(p[mid + 1] - p[mid]) * (k - k // 2 - 1)  # 每个数到心中都减少了p[mid+1]-p[mid]
            res = min(res, summ)

        # 不是把所有的点都移到“中心”位置x，而是把所有的点移到以x为中心的连续k个位置 --> 需要减去长度k移到最中心的距离
        offset = 0
        for i in range(k):
            offset += abs(i - k // 2)

        return res - offset