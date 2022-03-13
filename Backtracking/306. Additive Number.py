class Solution:
    # 给一个数字，判断能否把他分为至少三段使得第三段为前两段的和 --> 用path + 每段
    # 要么长度为1 要么第一位不能为0
    # 如果已经分为三段且后面没有数了---> True
    # 如果已经分为三段 但第三段不为前两段的和 ---> False

    def isAdditiveNumber(self, num: str) -> bool:
        return self.dfs(num, [])

    def dfs(self, num, path):
        if len(path) >= 3 and path[-1] != path[-2] + path[-3]:
            return False

        if not num and len(path) >= 3:
            return True

        for i in range(1, len(num) + 1):
            if num[0] != '0' or i == 1:
                if self.dfs(num[i:], path + [int(num[:i])]):
                    return True
        return False

