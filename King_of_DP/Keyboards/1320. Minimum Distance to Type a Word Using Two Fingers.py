class Solution:
    def minimumDistance(self, word: str) -> int:
        # 两根手指 --> 打完所有字的最短距离 --> either use left finger or right finger

        memo = {}
        return self.dfs(word, -1, -1, 0, memo)

    def dfs(self, word, l, r, pos, memo):
        if (l, r, pos) in memo:
            return memo[(l, r, pos)]

        if pos == len(word):
            return 0

        nxt = word[pos].lower()
        # left finger or right finger
        left_finger = self.dfs(word, nxt, r, pos + 1, memo) + self.getCost(l, nxt)
        right_finger = self.dfs(word, l, nxt, pos + 1, memo) + self.getCost(r, nxt)

        memo[(l, r, pos)] = min(left_finger, right_finger)
        return memo[(l, r, pos)]

    def getCost(self, a, b):
        if a == -1 or b == -1:
            return 0
        else:
            # 求 a 的数字距离 和 b 的数字距离
            aa = ord(a) - ord('a')
            bb = ord(b) - ord('a')
            # 求a和b分别在 在哪一行(//6) 哪一列（%6） --->求distance |x1 - x2| + |y1 - y2|
            return abs(aa // 6 - bb // 6) + abs(aa % 6 - bb % 6)


