class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # add gas - cost gas ---> net gas
        n = len(gas)
        summ = 0
        for i in range(n):
            summ += gas[i] - cost[i]

        if summ < 0:
            return -1

        tank = 0
        startpoint = 0
        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:  # can't reach from startpoint to i+1, should reset startpoint as i+1
                tank = 0
                startpoint = i + 1

        if startpoint == n:  # i + 1 --> index 即第0个位置
            return 0
        return startpoint