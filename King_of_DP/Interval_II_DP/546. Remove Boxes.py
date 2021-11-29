class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        # 找重复数字的区间，每次移除区间k得到k*k成绩，求怎么移除使得得分最大
        memo = {}
        return self.dfs(boxes, 0, len(boxes) - 1, 0, memo)

    def dfs(self, boxes, i, j, k, memo):
        if (i, j, k) in memo:
            return memo[(i, j, k)]

        if i > j:
            return 0

        # i 和 j 表示index，k表示重复数字的个数
        # 先找出左半边有多少重复的数字，count + 1
        while i < j and boxes[i] == boxes[i + 1]:
            i += 1
            k += 1
        # CASE1: 先消除左边，不合并
        res = self.dfs(boxes, i + 1, j, 0, memo) + (k + 1) * (k + 1)

        # CASE2： 先消除中间，然后合并左边和右边重复值 一起消除
        # 再找出 右半边是否有以相同boxes[i]结尾的，先消除中间部分，连接左半部分 count 在原来基础上增加
        # 111xxxxx1xxxx
        for mid in range(i + 1, j + 1):
            if boxes[i] == boxes[mid]:
                res = max(res, self.dfs(boxes, i + 1, mid - 1, 0, memo) + self.dfs(boxes, mid, j, k + 1, memo))
        memo[(i, j, k)] = res
        return memo[(i, j, k)]


class Solution1:
    def removeBoxes(self, boxes: List[int]) -> int:
        memo = {}
        return self.dfs(boxes, 0, len(boxes) - 1, 0, memo)

    def dfs(self, boxes, i, j, k, memo):
        if (i, j, k) in memo:
            return memo[(i, j, k)]

        if i > j:
            return 0

        while i < j and boxes[i] == boxes[i + 1]:
            i += 1
            k += 1

        # CASE1: not merge
        not_merge = self.dfs(boxes, i + 1, j, 0, memo) + (k + 1) * (k + 1)

        # CASE2: merge
        merge = float('-inf')
        for m in range(i + 1, j + 1):
            if boxes[i] == boxes[m]:
                merge = max(merge, self.dfs(boxes, i + 1, m - 1, 0, memo) + self.dfs(boxes, m, j, k + 1, memo))

        memo[(i, j, k)] = max(merge, not_merge)
        return memo[(i, j, k)]


class Solution:
    def removeBoxes(self, boxes) -> int:
        @functools.lru_cache(None)
        def dfs(i, j, k):
            if i > j:
                return 0
            while i + 1 <= j and boxes[i] == boxes[i + 1]:
                i += 1
                k += 1
            res = (k + 1) * (k + 1) + dfs(i + 1, j, 0)

            for mid in range(i + 1, j + 1):
                if boxes[i] == boxes[mid]:
                    res = max(res, dfs(i + 1, mid - 1, 0) + dfs(mid, j, k + 1))
            return res

        return dfs(0, len(boxes) - 1, 0)

