class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        memo = {}
        return self.dfs(s, k, 0, '', 0, memo)

    def dfs(self, s, k, pos, prev, prev_count, memo):
        if (k, pos, prev, prev_count) in memo:
            return memo[(k, pos, prev, prev_count)]

        if k < 0:
            return float('inf')

        if pos >= len(s):
            return 0

        if s[pos] == prev:
            if prev_count == 1 or prev_count == 9 or prev_count == 99:
                incr = 1
            else:
                incr = 0
            memo[(k, pos, prev, prev_count)] = self.dfs(s, k, pos + 1, prev, prev_count + 1, memo) + incr
            return memo[(k, pos, prev, prev_count)]
        else:
            keep = self.dfs(s, k, pos + 1, s[pos], 1, memo) + 1
            delete = self.dfs(s, k - 1, pos + 1, prev, prev_count, memo)
            memo[(k, pos, prev, prev_count)] = min(keep, delete)
            return memo[(k, pos, prev, prev_count)]


class Solution2:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # aaaabcccd --> a4bc3d
        # 对于每一个 s[pos] 要么 delete 要么 keep
        # 如果delete --> 整个compression的长度只有要delete 一个单独的letter的时候 才会发生变化。即s[pos] != prev
        # 当同一个letter的个数达到1+，9+，99+，整个compression的长度才会改变 +1

        memo = {}
        return self.dfs(s, k, 0, "", 0, memo)

    def dfs(self, s, k, pos, prev, prev_count, memo):
        if (k, pos, prev, prev_count) in memo:
            return memo[(k, pos, prev, prev_count)]

        if k < 0:
            return float('inf')

        if pos == len(s):
            return 0

        if s[pos] == prev:
            if prev_count == 1 or prev_count == 9 or prev_count == 99:
                incr = 1
            else:
                incr = 0

            keep = self.dfs(s, k, pos + 1, prev, prev_count + 1, memo) + incr


        else:
            keep = self.dfs(s, k, pos + 1, s[pos], 1, memo) + 1
        delete = self.dfs(s, k - 1, pos + 1, prev, prev_count, memo)

        memo[(k, pos, prev, prev_count)] = min(keep, delete)
        return memo[(k, pos, prev, prev_count)]