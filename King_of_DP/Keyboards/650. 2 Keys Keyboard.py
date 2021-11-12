class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}
        return self.dfs(n, 1, 0, memo)

    def dfs(self, n, curA, clipboard, memo):
        if (curA, clipboard) in memo:
            return memo[(curA, clipboard)]

        if curA > n:
            return float('inf')

        if curA == n:
            return 0

        # 只有还没复制的时候，才可以复制。不然死循环
        copy = float('inf')
        if curA != clipboard:
            copy = self.dfs(n, curA, curA, memo) + 1

            # 只有复制版上有东西的时候，才可以粘贴。不然死循环
        paste = float('inf')
        if clipboard and curA + clipboard <= n:
            paste = self.dfs(n, curA + clipboard, clipboard, memo) + 1

        memo[(curA, clipboard)] = min(copy, paste)
        return memo[(curA, clipboard)]