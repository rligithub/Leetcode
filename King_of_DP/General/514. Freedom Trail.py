import collections
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # 一个圆盘，每次需要转动圆盘使得12点的指针指向 所需的字母，左转右转都可。给出只要的key，求min step to get key
        # 变量 --> pos (key's index) and 12点的指针指向的ring的index值

        str_index = collections.defaultdict(list)
        for i, ch in enumerate(ring):
            str_index[ch].append(i)

        memo = {}

        return self.dfs(ring, str_index, key, 0, 0, memo)

    def dfs(self, ring, str_index, key, pos, point_to, memo):
        if (pos, point_to) in memo:
            return memo[(pos, point_to)]

        if pos == len(key):
            return 0

        n = len(ring)

        res = float('inf')
        for index in str_index[key[pos]]:
            cost = min(abs(index - point_to), n - abs(index - point_to)) + 1
            res = min(res, self.dfs(ring, str_index, key, pos + 1, index, memo) + cost)

        memo[(pos, point_to)] = res
        return memo[(pos, point_to)]