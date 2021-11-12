class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # 给两个数组 arr1 和 arr2，可以 swap arr1和arr2中的数字，求swap几个数字 使得arr1成为一个递增的序列
        # swap --> count + 1, prev = arr2[j]
        # not_swap --> count , prev = arr1[i]

        arr2 = sorted(set(arr2))
        memo = {}

        res = self.dfs(arr1, arr2, 0, float('-inf'), memo)

        if res != float('inf'):
            return res
        else:
            return -1

    def dfs(self, arr1, arr2, i, prev, memo):
        if (i, prev) in memo:
            return memo[(i, prev)]

        if i >= len(arr1):
            return 0
        # 在arr2 中找比prev大的第一个数的index --> 如果找不到的话，系统的bisect返回一个len 长度，超过 len - 1
        j = bisect.bisect_right(arr2, prev)

        swap, noswap = float('inf'), float('inf')
        # 检查是否找到 j 值
        if j < len(arr2):
            swap = self.dfs(arr1, arr2, i + 1, arr2[j], memo) + 1
        if arr1[i] > prev:
            noswap = self.dfs(arr1, arr2, i + 1, arr1[i], memo)

        memo[(i, prev)] = min(swap, noswap)
        return memo[(i, prev)]



