class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 正负号问题, 加小数点的情况, 比如 8/ 2 不需要加小数点, 小数部分,如何判断是否开始循环了 -->
        # 先判断结果的正负 --> 直接相除, 通过余数,看能否整除 --> 开始循环的时候, 说明之前已经出现过这个余数, 我们只要记录前面出现余数的位置,插入括号即可

        if numerator == 0: return "0"
        res = []
        # 首先判断结果正负, 异或作用就是 两个数不同 为 True 即 1 ^ 0 = 1 或者 0 ^ 1 = 1
        if (numerator > 0) ^ (denominator > 0):
            res.append("-")
        numerator, denominator = abs(numerator), abs(denominator)
        # 判读到底有没有小数
        a, b = divmod(numerator, denominator)
        res.append(str(a))
        # 无小数
        if b == 0:
            return "".join(res)
        res.append(".")
        # 处理余数
        # 把所有出现过的余数记录下来
        hashmap = {b: len(res)}  # {余数:index}
        while b:
            b *= 10
            a, b = divmod(b, denominator)
            res.append(str(a))
            # 余数前面出现过,说明开始循环了,加括号
            if b in hashmap:
                res.insert(hashmap[b], "(")
                res.append(")")
                break
            # 在把该位置的记录下来
            hashmap[b] = len(res)

        return "".join(res)
