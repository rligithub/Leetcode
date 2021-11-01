class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        # 求不同子字符串 substr格式 a + a
        # 奇数长度不符合条件
        n = len(text)

        res = set()
        for length in range(2, n + 1, 2):
            for i in range(n - length + 1):
                j = i + length // 2

                if text[i:j] == text[j:i + length]:
                    res.add(text[i:j])

        return len(res)