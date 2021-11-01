class Solution1:  # LTE
    def minOperations(self, target: List[int], arr: List[int]) -> int:

        # 给一个target的数组，求需要在另一个数组arr里添加几个数 才能使得target是arr的subsequence （相对顺序不变）
        # step1：先在arr里标记 target里的数的index，其他的为 -1，求 最长递增序列的 index
        # step2：target数组的长度 - 最长递增序列的index长度 ==》 需要操作几步

        if not target:
            return 0
        if not arr:
            return len(target)

        # step1 --> save target num and index in hashmap
        hashmap = {}
        for i, num in enumerate(target):
            hashmap[num] = i

        n = len(arr)
        # step2 --> 把相同value的index值保存起来, 比较相对顺序
        index = [-1] * n

        for i in range(n):
            if arr[i] in hashmap:
                index[i] = hashmap[arr[i]]

        # step3 --> find LIS for index ---> LTE if use dp
        dp = [1] * n

        for i in range(n):
            if index[i] == -1:
                dp[i] = 0
                continue
            for j in range(i):
                if index[i] > index[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return len(target) - max(dp)


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:

        # step1 --> save target num and index in hashmap
        hashmap = {}
        for i, num in enumerate(target):
            hashmap[num] = i

        n = len(arr)

        # step2 --> 把相同value的index值保存起来, 比较相对顺序 (剪枝 -->不需要存不同的数)
        res = []

        for i in range(n):
            if arr[i] in hashmap:
                res.append(hashmap[arr[i]])

        # step3: find LIS for res --> use binary search
        s = []
        for r in res:
            pos = bisect.bisect_left(s, r)
            if pos == len(s):
                s.append(r)
            else:
                s[pos] = r
        return len(target) - len(s)


class Solution3:
    def minOperations(self, target: List[int], arr: List[int]) -> int:

        table = {}
        for i, num in enumerate(target):
            table[num] = i

        dp = []
        for num in arr:
            if num in table:
                dp.append(table[num])
        return len(target) - self.lis(dp)

    def lis(self, nums):
        dp = []
        for num in nums:
            i = bisect.bisect_left(dp, num)
            if i >= len(dp):
                dp.append(num)
            else:
                dp[i] = num
        return len(dp)