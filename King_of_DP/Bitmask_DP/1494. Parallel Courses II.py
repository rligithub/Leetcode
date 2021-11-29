class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        # check each course's pre-requsition courses --> use bitmask
        # for loop each course to see which course can be taken --> save it in a pool
        # for loop a pool, get the combination --> mark down studied courses

        prereq = collections.defaultdict(int)
        for u, v in relations:
            prereq[v - 1] |= (1 << u - 1)

        memo = {}
        return self.dfs(n, k, prereq, 0, memo)

    def dfs(self, n, k, prereq, state, memo):
        if state in memo:
            return memo[state]

        if state == (1 << n) - 1:
            return 0

        studypool = []
        for i in range(n):
            if state & (1 << i):  # learned
                continue
            if state & prereq[i] == prereq[i]:
                studypool.append(i)

        res = float('inf')
        for comb in itertools.combinations(studypool, min(k, len(studypool))):
            nxtstate = state
            for course in comb:
                nxtstate |= (1 << course)
            res = min(res, self.dfs(n, k, prereq, nxtstate, memo) + 1)

        memo[state] = res
        return memo[state]

