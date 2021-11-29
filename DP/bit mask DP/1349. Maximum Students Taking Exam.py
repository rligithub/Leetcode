class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        # convert valid seats to bit mask

        m, self.n = len(seats), len(seats[0])
        validseat = [0] * m

        for i in range(m):
            for j in range(self.n):
                if seats[i][j] == '.':
                    validseat[i] = validseat[i] | (1 << j)

        memo = {}
        return self.dfs(validseat, 0, 0, memo)

    def dfs(self, validseat, pre_seats, pos, memo):
        if (pre_seats, pos) in memo:
            return memo[(pre_seats, pos)]

        # base case --> 走到最后一排
        if pos == len(validseat):
            return 0

        # for loop each row, check if row i right is valid, check if row i-1 right is valid, check if row i-1 left is valid
        # res -- > # of people sit in row[0...pos]
        res = 0
        for cur_seats in range(1 << self.n):
            # 如果 cur座位 & valid座位 == cur座位， 说明都为1，都是valid座位，可以坐
            # 如果 cur座位 & cur座位左移一位 == 0， 说明cur座位没有相邻的
            # 如果 pre座位 & cur座位左移一位 == 0， pre座位 & cur座位右移一位 == 0 ， 说明cur没有和prev对角座位
            if cur_seats & validseat[pos] == cur_seats and cur_seats & (cur_seats << 1) == 0 and pre_seats & (
                    cur_seats >> 1) == 0 and pre_seats & (cur_seats << 1) == 0:
                res = max(res, self.dfs(validseat, cur_seats, pos + 1, memo) + bin(cur_seats).count('1'))

        memo[(pre_seats, pos)] = res
        return memo[(pre_seats, pos)]

    def bit_count(n):
        cnt = 0
        while n:
            n &= n - 1
            cnt += 1
        return cnt
