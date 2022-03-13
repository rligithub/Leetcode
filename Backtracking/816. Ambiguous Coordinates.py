class Solution1:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        # 把一个string变成一个坐标 --> 分为两段,用逗号隔开,每个数可以变为小数
        # step1: 先拆分所有的数字，分为x和y，检查是否有效，无效的去除
        # step2: 对拆出的数字进行加.处理 1) 如果第一个字符为0 那么 要么这个数字是 0 要么这个数字是 0.xxx 2) 如果结尾是0 那么这个数不能是是小数

        res = []
        s = s[1:-1]  # exclude "(" and ")"
        # break down by two parts
        for i in range(1, len(s)):  # length
            x_list = self.getallpossible(s[:i])
            y_list = self.getallpossible(s[i:])
            for i in x_list:
                for j in y_list:
                    res.append("(" + i + ', ' + j + ")")  # res.append("(%s, %s)" % (i,j))
        return res

    def getallpossible(self, s: str):

        # CASE1: 如果第一个字符为0 那么 要么这个数字是 0 要么这个数字是 0.xxx
        if s != '0' and s[0] == '0':  # if first digit is 0 and there is digits after 0
            if s[-1] != '0':  # if last digit is not 0 --> add '.'
                return ["0." + s[1:]]
            else:  # if last digit is 0 --> not add '.'
                return []

        # CASE2: 如果结尾是0 那么这个数不能是是小数
        if s[-1] == '0':  # if last digit is 0 --> not add '.'
            return [s]

        res = [s]
        for i in range(1, len(s)):
            res.append(s[:i] + "." + s[i:])
        return res

