class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        # 每种 button不同功能，求按presses下后出现的不同可能性有几个 --> 每次按button，就 当前状态^button
        res = set()
        state = int('1' * n)
        button = {
            1: int(''.join(['1' for i in range(n)])),
            2: int(''.join(['1' if (i + 1) % 2 == 0 else '0' for i in range(n)])),
            3: int(''.join(['1' if (i + 1) % 2 == 1 else '0' for i in range(n)])),
            4: int(''.join(['1' if (i + 1) % 3 == 1 else '0' for i in range(n)])),
        }

        memo = {}
        self.dfs(state, presses, res, button, memo)
        return len(res)

    def dfs(self, state, k, res, button, memo):
        if (state, k) in memo:
            return memo[(state, k)]
        if len(res) >= 8:
            return

        if k == 0:
            res.add(state)
            return

        for i in range(1, 5):
            self.dfs(state ^ button[i], k - 1, res, button, memo)
            memo[(state, k)] = res