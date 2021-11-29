class Solution1:  # fast
    def mergeStones(self, stones: List[int], k: int) -> int:
        # 合并"连续"的k堆石头成为一堆
        # check if there is solutions
        # 检查是否可以刚好分配 ___|__|__|__|__| ----> 每三个石头合并为一堆，最后剩一堆 (n - 1) % (k-1)
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

            # prefix sum
        presum = [0]
        for stone in stones:
            total = presum[-1] + stone
            presum.append(total)

        # i, j --> start index, end index
        memo = {}
        return self.dfs(stones, presum, k, 0, len(stones) - 1, memo)

    def dfs(self, stones, presum, k, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # base case --> last piles is less than k piles
        size = j - i + 1
        if size < k:
            return 0

        res = float('inf')
        # merge every k piles, m += k - 1
        for m in range(i, j, k - 1):
            res = min(res, self.dfs(stones, presum, k, i, m, memo) + self.dfs(stones, presum, k, m + 1, j, memo))

        # valid size --> last pile cost = all sum
        if (size - 1) % (k - 1) == 0:
            res += presum[j + 1] - presum[i]

        memo[(i, j)] = res
        return memo[(i, j)]


class Solution:  # 3D dp --> 最后分为 p堆
    def mergeStones(self, nums, k: int) -> int:
        # presum
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        # i, j, p --> start index, end index, 把石头堆分为几份（2-k之间）
        memo = {}
        res = self.dfs(k, presum, 0, len(nums) - 1, 1, memo)
        return res if res != float('inf') else -1

    def dfs(self, k, presum, i, j, p, memo):
        if (i, j, p) in memo:
            return memo[(i, j, p)]

        # 检查是否可以刚好分配 ___|__|__|__|___ 每三个石头合并为一堆，最后剩两堆 --> (n - 2) % (k-1)
        if (j - i + 1 - p) % (k - 1) != 0:
            return float('inf')

        # 如果只剩一个石头，只能合并为一堆，不能合并成 p > 1 堆
        if i == j:
            if p == 1:
                return 0
            else:
                return float('inf')

        # 合并成一堆，所需要的cost
        if p == 1:
            return self.dfs(k, presum, i, j, k, memo) + presum[j + 1] - presum[i]

        res = float('inf')
        for m in range(i, j, k - 1):
            res = min(res, self.dfs(k, presum, i, m, 1, memo) + self.dfs(k, presum, m + 1, j, p - 1, memo))

        memo[(i, j, p)] = res
        return res