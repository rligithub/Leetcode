class Solution1:  # approach # 1
    def maxA(self, n: int) -> int:
        # how many A in screen --> add one / add all(ctrlA+C+P) / add whatever(ctrlP)
        @functools.lru_cache(None)
        def dfs(n, curA, buffer):

            if n <= 0:
                return curA

            add_one, add_all, add = float('-inf'), float('-inf'), float('-inf')
            # paste one A
            if buffer == 0:
                add_one = dfs(n - 1, curA + 1, buffer)
            # paste whatever in clipboard
            if buffer:
                add_all = dfs(n - 1, curA + buffer, buffer)
            # select + copy + paste
            if n - 3 >= 0:
                add = dfs(n - 3, curA * 2, curA)

            return max(add_one, add_all, add)

        return dfs(n - 1, 1, 0)


class Solution2:  # approach #2
    def maxA(self, n: int) -> int:
        memo = {}
        return self.dfs(n, 0, 0, memo)

    def dfs(self, n, curA, buffer, memo):
        if (n, curA, buffer) in memo:
            return memo[(n, curA, buffer)]

        if n <= 0:
            return curA

        add_one, add_all, copy = float('-inf'), float('-inf'), float('-inf')

        # paste one A --> best case, only when no value in clipboard
        if buffer == 0:
            add_one = self.dfs(n - 1, curA + 1, buffer, memo)
        # paste A in clipboard
        if buffer:
            add_all = self.dfs(n - 1, curA + buffer, buffer, memo)
        # select + copy A in clipboard --> copy when there is A in screen
        if curA:
            copy = self.dfs(n - 2, curA, curA, memo)

        memo[(n, curA, buffer)] = max(add_one, add_all, copy)
        return memo[(n, curA, buffer)]


class Solution1:
    def maxA(self, n: int) -> int:
        # how many A in screen --> add one / add all(ctrlA+C+P) / add whatever(ctrlP)
        @functools.lru_cache(None)
        def dfs(n, curA, buffer):

            if n <= 0:
                return curA

            add_one, add_all, add = float('-inf'), float('-inf'), float('-inf')
            # paste one A
            if buffer == 0:
                add_one = dfs(n - 1, curA + 1, buffer)
            # paste whatever in clipboard
            if buffer:
                add_all = dfs(n - 1, curA + buffer, buffer)
            # select + copy
            if curA:
                add = dfs(n - 2, curA, curA)

            return max(add_one, add_all, add)

        return dfs(n, 0, 0)