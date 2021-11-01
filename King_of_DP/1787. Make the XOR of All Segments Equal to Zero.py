class Solution1:
    def minChanges(self, nums: List[int], k: int) -> int:
        # XXX XXX XXX
        # A1^A2^A3 = 0
        # A2^A3^A4 = 0
        # --> A1 == A4, A2 == A5, A3 == A6 ...
        # same value Ai = A(i+k) = A[i+2k] = A[i+3k]...

        # 求每个k个数为一组，每组中每个数出现的频率
        n = len(nums)
        count = collections.defaultdict(collections.Counter)
        for i in range(k):
            for j in range(i, n, k):
                count[i][nums[j]] += 1

        # 每组数的众数  --> 频率最高的数
        table = [count[i].most_common(1)[0][1] for i in range(k)]

        # 每组全部变为同样的数的最小代价
        ans = n - sum(table)

        # 每组数都是众数，要满足异或为0，需要统计每组数选哪个数达到最优解，或者牺牲哪组数
        @functools.lru_cache(None)
        def dfs(pos, cur_XOR):
            if pos == k and cur_XOR == 0:
                return 0
            if pos == k and cur_XOR != 0:
                return float("inf")
            # 牺牲这组数的额外代价,所有数都换为某个数，使得异或为0

            res = table[pos]
            # 变为这组数中的某个数
            for key in count[pos].keys():
                res = min(res, dfs(pos + 1, cur_XOR ^ key) - count[pos][key] + table[pos])
            return res

        return ans + dfs(0, 0)


class Solution:  # TLE
    def minChanges(self, nums: List[int], k: int) -> int:
        # 求每个k个数为一组，每组中每个数出现的频率
        n = len(nums)
        count = collections.defaultdict(collections.Counter)
        for i in range(k):
            for j in range(i, n, k):
                count[i][nums[j]] += 1

        # 每组数的众数  --> 频率最高的数
        table = [count[i].most_common(1)[0][1] for i in range(k)]
        # 每组全部变为同样的数的最小代价
        ans = n - sum(table)
        memo = {}
        return ans + self.dfs(table, count, k, 0, 0, memo)

    def dfs(self, table, count, k, i, curr, memo):
        if (i, curr) in memo:
            return memo[(i, curr)]
        if i == k and curr == 0:
            return 0
        elif i == k:
            return float("inf")
        # 牺牲这组数的额外代价,所有数都换为某个数，使得异或为0
        res = table[i]
        # 变为这组数中的某个数
        for key in count[i].keys():
            res = min(res, self.dfs(table, count, k, i + 1, curr ^ key, memo) - count[i][key] + table[i])
        memo[(i, curr)] = res
        return memo[(i, curr)]

