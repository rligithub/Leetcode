class Solution1:  # TLE
    def waysToDistribute(self, n: int, k: int) -> int:
        memo = {}
        return self.dfs(n, k, memo)

    def dfs(self, n, k, memo):
        if (n, k) in memo:
            return memo[(n, k)]

        if n < k:
            return 0

        if n == 0 and k == 0:
            return 1

        if n == 0 or k == 0:
            return 0

        mod = 10 ** 9 + 7

        # n - 1 are all distributed in k bages, last one can be put in any bag
        anybag = self.dfs(n - 1, k, memo) * k

        # n - 1 are all distributed in k - 1 bages, last one can only be put in last bag
        lastbag = self.dfs(n - 1, k - 1, memo)

        memo[(k, pos)] = (anybag + lastbag) % mod
        return memo[(k, pos)]


class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(n, k):
            if n == 0 and k == 0:
                return 1

            if n == 0 or k == 0 or k > n:
                return 0

                # n - 1 are all distributed in k bages, last one can be put in any bag
            anybag = dfs(n - 1, k) * k

            # n - 1 are all distributed in k - 1 bages, last one can only be put in last bag
            lastbag = dfs(n - 1, k - 1)

            return (anybag + lastbag) % mod

        res = dfs(n, k) % mod
        dfs.cache_clear()
        return res


class Solution3:  # TLE
    def waysToDistribute(self, n: int, k: int) -> int:
        memo = {}
        return self.dfs(n, k, 0, 0, memo)

    def dfs(self, n, k, candy, bag, memo):
        if (candy, bag) in memo:
            return memo[(candy, bag)]

        # n - 1 are all distributed in k bages, last one can be put in any bag
        # n - 1 are all distributed in k - 1 bages, last one can only be put in last bag
        if bag > n or bag > k:
            return 0

        if candy == n:
            if bag == k:
                return 1
            else:
                return 0

        mod = 10 ** 9 + 7

        samebag = self.dfs(n, k, candy + 1, bag, memo) * bag

        diffbag = self.dfs(n, k, candy + 1, bag + 1, memo)

        memo[(candy, bag)] = (samebag + diffbag) % mod
        return memo[(candy, bag)]


class Solution4:
    def waysToDistribute(self, n: int, k: int) -> int:

        mod = 10 ** 9 + 7
        self.n = n
        self.k = k

        @functools.lru_cache(None)
        def dfs(n, k):
            if k > n or k > self.k:
                return 0

            if n >= self.n:
                if k == self.k:
                    return 1
                return 0

            res = 0
            res += dfs(n + 1, k + 1)
            res += k * dfs(n + 1, k)
            return res % mod

        res = dfs(0, 0) % mod
        dfs.cache_clear()
        return res