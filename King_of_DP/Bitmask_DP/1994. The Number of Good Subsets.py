class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        # 找出每个num的出现的个数 count
        # 找出总共有几个质数
        # 找出每个num能够被哪些质数整除（求这几个质数的对于bit位置--> mask）
        # dp存每个质数是否出现的状态 --> for loop每种状态，先检查不能有重复质数出现（位置不能重合），求每种状态下能有几种可能性 --> 从大到小 dp[state] = dp[state - mask] * count[num]
        # OR 从小到大 dp[state | mask] = dp[state] *count[num]

        cnt = Counter(nums)
        mod = 10 ** 9 + 7
        # 30以内质数：[2,3,5,7,11,13,17,19,23,29]
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        # dp[i]表示满足nums中符合条件质数分布的数目
        m = len(prime)
        dp = [0] * (1 << m)

        # initialization --> empty subset
        dp[0] = 1
        for num in cnt:
            # 先排除 num == 1 的情况，因为1可以和任何num组合
            if num == 1:
                continue
            # 排除 num由两个相同质数组成的情况（不选）
            if any(num % (p * p) == 0 for p in prime):
                continue

            mask = 0
            # 找出该num 能被够哪些不同的质数整除。用mask标记出现所有整除质数的位置（总的list）
            for i in range(m):
                if num % prime[i] == 0:
                    mask |= 1 << i

            # 对于每种状态， 找出不符合条件的状态 --> 从小到大
            for i in range(1 << m):
                # 找出不包含 组合成num的质数 的状态（题目要求subset不能有重复质数出现）--> 该subset+组成num质数的subset = 该subset的个数 *(num出现的个数)
                if i & mask == 0:
                    dp[i | mask] += dp[i] * cnt[num]
                    dp[i | mask] %= mod
        res = sum(dp) - 1  # empty subset
        return (2 ** cnt[1]) * res % mod
 

class Solution2:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        mod = 10 ** 9 + 7
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        m = len(prime)
        dp = [0] * (1 << m)
        dp[0] = 1
        for num in cnt:
            if num == 1:
                continue

            if any(num % (p * p) == 0 for p in prime):
                continue

            mask = 0
            for i in range(m):
                if num % prime[i] == 0:
                    mask |= 1 << i

            for state in range((1 << m) - 1, 0, -1):  # 从大到小

                if state - mask == state ^ mask:
                    dp[state] += dp[state - mask] * cnt[num]
                    dp[state] %= mod

        return (1 << cnt[1]) * (sum(dp) - 1) % mod


class Solution2: # topdown - unknown
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        counts = collections.Counter(nums)
        mod = 10 ** 9 + 7
        indexP = {}
        for i, p in enumerate(primes):  # primes in bits
            indexP[p] = i
        print(indexP)
        # the bitmask of each num, store in bits
        bitmaskNum = {}
        # find the bitmask for each num
        for num in counts:
            if num == 1:
                continue
            cur = 0
            for p in primes:
                if num % p == 0:
                    if num % (p ** 2) == 0:
                        break
                    cur = cur | (1 << indexP[p])
            else:

                bitmaskNum[num] = cur
        # that is the list of distinct numbers, except 1
        keys = sorted(bitmaskNum.keys())

        memo = {}
        res = self.dfs(keys, bitmaskNum, counts, 0, 0, 0, memo)
        if 1 in counts:  # reconsider 1
            res = res * (pow(2, counts[1])) % mod
        return res

    def dfs(self, keys, bitmaskNum, counts, pos, visited, cur, memo):
        # starting from index，with visited nums，and cur primes
        if (pos, visited) in memo:
            return memo[(pos, visited)]

        # if it comes to the end, we need to check whether we visited nums
        if pos == len(keys):
            return int(visited != 0)

        mod = 10 ** 9 + 7

        # directly go to the end
        not_pick = self.dfs(keys, bitmaskNum, counts, len(keys), visited, cur, memo)

        pick = 0
        for i in range(pos, len(keys)):
            if cur & bitmaskNum[
                keys[i]] == 0:  # if nums[i] doesn't have common bitmaskNum, update the visited and primes pool
                pick += self.dfs(keys, bitmaskNum, counts, i + 1, visited | 1 << i, cur | bitmaskNum[keys[i]], memo) * \
                        counts[keys[i]]

        memo[(pos, visited)] = (pick + not_pick) % mod
        return memo[(pos, visited)]

