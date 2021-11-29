import collections


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        # how to allocate hats to each person ===> check if everyone has hats

        # convert to who wants the hats
        # for loop hats to see who wants the hats, give hats to people who don't have hats.

        peopleHats = collections.defaultdict(list)

        for p, hat in enumerate(hats):
            for h in hat:
                peopleHats[h].append(p)

        fullMask = (1 << len(hats)) - 1

        memo = {}
        return self.dfs(peopleHats, fullMask, 0, 0, memo)

    def dfs(self, peopleHats, fullMask, state, pos, memo):
        if (state, pos) in memo:
            return memo[(state, pos)]
        if state == fullMask:
            return 1

        if pos >= 41:
            return 0

        mod = 10 ** 9 + 7

        not_pick = self.dfs(peopleHats, fullMask, state, pos + 1, memo)

        pick = 0
        for p in peopleHats[pos]:
            if state & (1 << p):
                continue
            pick += self.dfs(peopleHats, fullMask, state | (1 << p), pos + 1, memo)

        memo[(state, pos)] = (not_pick + pick) % mod
        return memo[(state, pos)]