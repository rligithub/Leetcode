class Solution:  # TLE
    def minimumTimeRequired(self, jobs, k):
        # each worker gets a subset of tasks
        # remaining subproblem = bitmask of remaining tasks, k-1
        # enumerate all subsets for each worker
        # make sure no intersection with already selected
        n = len(jobs)

        time = [0] * (1 << (n))
        for state in range(1 << (n)):
            for j in range(n):
                if state & (1 << j):
                    time[state] += jobs[j]
        memo = {}
        return self.dfs(jobs, time, 0, k, memo)

    def dfs(self, jobs, time, picked, k, memo):
        if (picked, k) in memo:
            return memo[(picked, k)]
        n = len(jobs)
        # return 0 if No job remaining AND No person remaining
        if k == 0 and picked + 1 == 1 << (n):
            return 0
        elif k == 0 or picked + 1 == 1 << (n):
            return float('inf')

        res = float('inf')
        for pick in range(1 << (n)):
            if pick & picked == 0:  # no intersection(picked again)
                # now assign remaining workers
                res = min(res, max(time[pick], self.dfs(jobs, time, picked | pick, k - 1, memo)))
        memo[(picked, k)] = res
        return memo[(picked, k)]


class Solution:
    def minimumTimeRequired(self, jobs, k):
        n = len(jobs)
        # preprocessing - total time spend on job for one worker, if he/she does different jobs
        time = [0] * (1 << (n))
        for state in range(1 << (n)):
            for j in range(n):
                if state & (1 << j):
                    time[state] += jobs[j]
        memo = {}
        return self.dfs(time, (1 << n) - 1, k, memo)

    def dfs(self, time, state, k, memo):
        if (state, k) in memo:
            return memo[(state, k)]

        if state == 0:
            return 0

        if k == 0:
            return float('inf')

        res = float('inf')
        substate = state
        while substate:
            if time[substate] < res:
                res = min(res, max(time[substate], self.dfs(time, state ^ substate, k - 1, memo)))

            substate = (substate - 1) & state
        memo[(state, k)] = res
        return memo[(state, k)]


