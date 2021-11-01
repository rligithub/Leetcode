class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # 求不同不连续子序列有多少个
        # 从左往右走，如果s[i] 没有在之前的数里，则新增的subsequences为之前的res，总数为res*2
        # 如果s[i]和之前的走过的char重复，则新增的subsequences总数需要减去之前那个repeat增加的subsequences
        # a b b
        # a --> "", a
        # b --> "", a,    b, ab
        # b --> "", a,    b, ab,    b, ab, bb, abc --> must minus increases due to first b (b, ab)
        # 需要记录 每次新增的数 + 累积总数

        hashmap = {}
        mod = 10 ** 9 + 7
        # reduce empty subsequences
        return self.dfs(s, 0, hashmap) % mod - 1

    def dfs(self, s, pos, hashmap):

        if pos == len(s):
            return 1

        base = self.dfs(s, pos + 1, hashmap)

        ch = s[pos]
        if ch not in hashmap:
            hashmap[ch] = base
            return base * 2
        else:
            res = base * 2 - hashmap[ch]
            # 更新repeat的字符 最近一次所增加的subsequences数（已经包括了第一次repeat）
            hashmap[ch] = base
            return res




