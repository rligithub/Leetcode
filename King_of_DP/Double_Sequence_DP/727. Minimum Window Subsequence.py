class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        # 用dfs找出 end index of subarry
        # for loop 找出 start index of subarry，然后找出最短的length
        l = float('inf')
        res = ''
        memo = {}
        for i, char in enumerate(s1):
            # 找出 第一个matched的char --> 剪枝
            if char == s2[0]:
                # 用dfs找出 对应 第二个以及之后的char的end index of subarray
                j = self.dfs(s1, s2, i, 1, memo)  # 必须从i开始，因为dfs搜索要用for loop +1 --> 相当于从 i+1 开始
                # 找出最短的长度 subarray
                if j - i < l:
                    l = j - i
                    res = s1[i:j + 1]

        return res

    def dfs(self, s1, s2, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # return end index of subarry of s1
        if j == len(s2):
            return i

            # find s2[j] value in s1[i+1:] 从i+1的位置上 开始找j位置的值 --> 相当于for loop
        k = s1.find(s2[j], i + 1)

        if k == -1:  # 没找到
            res = float('inf')
        else:
            res = self.dfs(s1, s2, k, j + 1, memo)  # 找到

        memo[(i, j)] = res
        return memo[(i, j)]


class Solution1:  # TLE
    def minWindow(self, s1: str, s2: str) -> str:
        # 用dfs找出 end index of subarry
        # for loop 找出 start index of subarry，然后找出最短的length
        l = float('inf')
        res = ''
        memo = {}
        for i, char in enumerate(s1):
            # 找出 第一个matched的char --> 剪枝
            if char == s2[0]:
                # 用dfs找出 对应 第二个以及之后的char的end index of subarray
                j = self.dfs(s1, s2, i, 1, memo)  # 必须从i开始，因为dfs搜索要用for loop +1 --> 相当于从 i+1 开始
                # 找出最短的长度 subarray
                if j - i < l:
                    l = j - i
                    res = s1[i:j + 1]

        return res

    def dfs(self, s1, s2, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # return end index of subarry of s1
        if j == len(s2):
            return i

        res = float('inf')
        for k in range(i + 1, len(s1)):
            if s1[k] == s2[j]:
                res = self.dfs(s1, s2, k, j + 1, memo)
                break

        memo[(i, j)] = res
        return memo[(i, j)]


a = Solution()
s1 = "abcdebde"
s2 = "bde"
print(a.minWindow(s1, s2))
