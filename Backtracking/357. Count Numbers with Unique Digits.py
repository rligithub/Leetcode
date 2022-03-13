class Solution1:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        memo = {}
        return self.dfs(n, 0, [0] * 10, memo)

    def dfs(self, n, i, visited, memo):
        if i in memo:
            return memo[i]
        if i == n:
            return 1

        res = 1
        for num in range(0, 10):
            if i == 0 and num == 0:  # no leading zero
                continue
            if visited[num]:  # de-duplicated
                continue
            visited[num] = True
            res += self.dfs(n, i + 1, visited, memo)
            visited[num] = False
        memo[i] = res
        return res


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        memo = {}
        return self.dfs(n, 0, set(), memo)

    def dfs(self, n, i, visited, memo):
        if i in memo:
            return memo[i]
        if i == n:
            return 1

        res = 1
        for num in range(0, 10):
            if i == 0 and num == 0:  # no leading zero
                continue
            if num in visited:  # de-duplicated
                continue
            visited.add(num)
            res += self.dfs(n, i + 1, visited, memo)
            visited.remove(num)
        memo[i] = res
        return res


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        memo = {}
        return self.dfs(n, 0, 0, memo)

    def dfs(self, n, i, state, memo):
        if state in memo:
            return memo[state]
        if i == n:
            return 1

        res = 1
        for num in range(0, 10):
            if i == 0 and num == 0:  # no leading zero
                continue
            if state & (1 << num):  # de-duplicated
                continue
            res += self.dfs(n, i + 1, state | (1 << num), memo)

        memo[state] = res
        return res