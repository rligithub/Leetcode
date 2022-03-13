class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # 用下标判断现在在处理的是小时还是分。另外提前判断是否是合法的时间，合法才继续递归(剪枝)

        arr = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        res = []

        self.dfs(turnedOn, arr, 0, 0, 0, res)
        return res

    def dfs(self, turnedOn, arr, h, m, pos, res):
        if turnedOn == 0:
            if m < 10:  # 分钟用两位数表示
                seconds = str(0) + str(m)
            else:
                seconds = str(m)
            res.append(str(h) + ':' + seconds)
            return

        for i in range(pos, 10):
            hour = h
            minute = m
            if i < 4:
                hour += arr[i]
            else:
                minute += arr[i]
            if hour < 12 and minute < 60:
                self.dfs(turnedOn - 1, arr, hour, minute, i + 1, res)
