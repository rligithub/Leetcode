class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 打印 ip 地址，分成4段，pos来表示第几段
        # 每段最多3位数， 要么长度为1 要么第一位不能为0 ，每段必须小等于255
        # 打印 --> 跑到第4段且后面没有数了
        res = []
        path = ''
        self.dfs(s, 0, path, res)
        return res

    def dfs(self, s, pos, path, res):
        if pos == 4 and not s:
            res.append(path[:-1])
            return

        for i in range(1, min(4, len(s) + 1)):
            if (i == 1 or s[0] != "0") and int(s[:i]) <= 255:
                self.dfs(s[i:], pos + 1, path + s[:i] + ".", res)




