class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        # assign bikes to each workers, bikes > workers. some of bikes may not be assigned
        # bikes --> 00000 ---> 11111 bikes assigned
        # for loop worker to see if bike is availble to be assigned --> compare distances

        memo = {}
        return self.dfs(workers, bikes, 0, 0, memo)

    def dfs(self, workers, bikes, state, w, memo):
        if (state, w) in memo:
            return memo[(state, w)]

        if w == len(workers):
            return 0

        res = float('inf')
        for b in range(len(bikes)):
            if state & (1 << b) == 0:
                res = min(res,
                          self.dist(workers, bikes, w, b) + self.dfs(workers, bikes, state | (1 << b), w + 1, memo))

        memo[(state, w)] = res
        return memo[(state, w)]

    def dist(self, workers, bikes, w, b):
        xw, yw = workers[w]
        xb, yb = bikes[b]
        return abs(xw - xb) + abs(yw - yb)