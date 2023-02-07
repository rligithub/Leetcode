class Solution:
    def countDistinct(self, s: str) -> int:
        n = len(s)
        base = 26
        mod = 2 ** 63 - 1

        seen = set()
        for i in range(n):
            hashcode = 1  # 初始值必须为1，因为如果为0的话，a和aa和aaa的hashcode是一样的
            for j in range(i, n):
                num = ord(s[j]) - ord("a")
                hashcode = (hashcode * base + num) % mod
                seen.add(hashcode)
        return len(seen)