class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        # state --> if the seats is empty in each row -->  people --> 1
        # must be in validSeat --> state[row] & validSeat[row] == state[ro]
        # 左上 不能坐人 --> state[row-1] & (state[row] << 1) == 0
        # 右上 不能坐人 --> state[row-1] & (state[row] >> 1) == 0
        # 左边 不能坐人 --> state[row] & (state[row] << 1) == 0
        # 右边 不能坐人 --> state[row] & (state[row] >> 1) == 0

        ''' validSeat:
        010 010
        100 001
        010 010
        '''

        m, n = len(seats), len(seats[0])

        # convert it to bitmask --> valid seats
        validSeat = [0] * m
        for i in range(m):
            for j in range(n):
                if seats[i][j] == '.':
                    validSeat[i] |= (1 << j)

        memo = {}
        return self.dfs(seats, validSeat, 0, 0, memo)

    def dfs(self, seats, validSeat, prevSeat, row, memo):
        if (prevSeat, row) in memo:
            return memo[(prevSeat, row)]

        if row == len(seats):
            return 0

        res = 0
        for curSeat in range(1 << len(seats[0])):  # sub-state of each row
            if curSeat & validSeat[row] == curSeat and curSeat & (curSeat << 1) == 0 and prevSeat & (
                    curSeat << 1) == 0 and prevSeat & (curSeat >> 1) == 0:
                res = max(res, self.dfs(seats, validSeat, curSeat, row + 1, memo) + bin(curSeat).count('1'))

        memo[(prevSeat, row)] = res
        return memo[(prevSeat, row)]





