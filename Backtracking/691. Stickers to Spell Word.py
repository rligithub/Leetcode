class Solution1:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # 和small team那题不同，target里的有重复的char，每个sticker不好转成对应target的bitmask表示 --> 用hashmap

        n = len(target)
        dp = collections.defaultdict(int)
        s = collections.Counter(target)
        A = [collections.Counter(stick) & s for stick in stickers]

        for i in range(len(A) - 1, -1, -1):
            if any(A[i] & A[j] == A[i] for j in range(len(A)) if i != j):
                A.pop(i)
        for i in range(1 << n):
            if dp[i] == 0 and i != 0:
                continue
            for a in A:
                nex = i
                has = a.copy()
                for pos in range(n):
                    if i & (1 << pos) != 0 or has[target[pos]] == 0:
                        continue
                    else:
                        nex |= (1 << pos)
                        has[target[pos]] -= 1
                if i != nex:
                    dp[nex] = dp[i] + 1 if dp[nex] == 0 else min(dp[nex], dp[i] + 1)
        return -1 if dp[(1 << n) - 1] == 0 else dp[(1 << n) - 1]


class Solution2:  # similar to #638 shopping offer
    def minStickers(self, stickers: List[str], target: str) -> int:
        needs = collections.defaultdict(int)
        counts = []

        # step1: convert all stickers to hashmap to record char had 
        for i, sticker in enumerate(stickers):
            sticker_count = collections.defaultdict(int)
            for char in sticker:
                sticker_count[tuple(char)] += 1
            counts.append(sticker_count)

        # step2: convert target to hashmap to record char needs     
        for char in target:
            needs[tuple(char)] += 1

        # step3: dfs to find needs 
        memo = {}
        res = self.dfs(stickers, counts, needs, memo)
        if res == float('inf'):
            return -1
        return res

    def dfs(self, stickers, counts, needs, memo):
        # 把hashmap sort好 --> 封装成string 才能用memo记录
        string = ''
        for key in sorted(needs.keys()):
            string += (str(key) + str(needs[key]))

        if string in memo:
            return memo[string]
        if len(needs) == 0:
            return 0

        res = float('inf')
        for i in range(len(counts)):
            remain_needs = collections.defaultdict(
                int)  # new hashmap to save remain_needs --> no need to mannually backtrack
            valid_sticker = False
            for char in needs.keys():
                if char in counts[i]:
                    valid_sticker = True
                    if counts[i][char] < needs[char]:
                        remain_needs[char] = needs[char] - counts[i][char]
                else:
                    remain_needs[char] = needs[char]

            if not valid_sticker:
                continue
            if valid_sticker:
                res = min(res, self.dfs(stickers, counts, remain_needs, memo) + 1)

        memo[string] = res
        return res


class Solution3:  # backtracking --> new remaining needs
    def minStickers(self, stickers, target: str) -> int:
        # pre-processing 
        counts = []
        for i, sticker in enumerate(stickers):
            sticker_count = collections.Counter(sticker)
            counts.append(sticker_count)

        self.res = float('inf')

        @functools.lru_cache(None)
        def dfs(target, count):
            needs = collections.Counter(target)
            if not needs:
                self.res = min(self.res, count)
                return

            for i in range(len(counts)):
                new_target = ''
                valid_sticker = False
                for char in needs.keys():
                    if char in counts[i]:
                        valid_sticker = True
                        if counts[i][char] < needs[char]:
                            new_target += (char * (needs[char] - counts[i][char]))
                    else:
                        new_target += (char * needs[char])

                if not valid_sticker:
                    continue
                if valid_sticker:
                    dfs(new_target, count + 1)

        dfs(target, 0)
        return self.res if self.res < float('inf') else -1


class Solution:  # bitmask
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        state = (1 << n) - 1

        @functools.lru_cache(None)
        def dfs(state):
            if state == 0:
                return 0

            x = 0
            while (1 << x) & state == 0:
                x += 1
            first_ch = target[x]

            res = -1
            for word in stickers:
                count = collections.Counter(word)
                if first_ch not in count:
                    # 每次只选包含边界上字符的单词，缩减枚举量，避免出现 stat1, stat2, stat3 和 stat2 stat1 stat3 这样的等效序列
                    # 有了这个剪枝条件，性能提升了10倍
                    continue

                newState = state
                for i in range(len(target)):
                    if newState & (1 << i) and target[i] in count and count[target[i]] > 0:
                        count[target[i]] -= 1
                        newState &= ~(1 << i)

                    if newState != state:
                        val = dfs(newState)
                        if val != -1 and (res == -1 or 1 + val < res):
                            res = 1 + val
            return res

        return dfs(state)