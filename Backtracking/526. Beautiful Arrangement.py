class Solution1:
    def countArrangement(self, n: int) -> int:
        # similar to 357 count numbers with unique digits
        return self.dfs(n, 1, set())

    def dfs(self, n, pos, visited):

        if pos == n + 1:
            return 1

        res = 0
        for num in range(1, n + 1):
            if num in visited:
                continue
            if num % pos != 0 and pos % num != 0:
                continue
            visited.add(num)
            res += self.dfs(n, pos + 1, visited)
            visited.remove(num)

        return res


class Solution:
    def countArrangement(self, n: int) -> int:
        # use state to keep track what num has been used --> visited

        memo = {}
        return self.dfs(n, 1, 0, memo)

    def dfs(self, n, pos, state, memo):
        if state in memo:
            return memo[state]
        if pos == n + 1:
            return 1

        res = 0
        for num in range(1, n + 1):
            if state & 1 << num:  # de-duplicated
                continue
            if num % pos != 0 and pos % num != 0:
                continue
            res += self.dfs(n, pos + 1, state | 1 << num, memo)

        memo[state] = res
        return res
