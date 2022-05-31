class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window

        size = float('inf')
        start = 0
        left, right = 0, 0

        window = collections.defaultdict(int)
        needs = collections.defaultdict(int)

        for ch in t:
            needs[ch] += 1

        match = 0
        while right < len(s):  # 先不断地增加 right 指针扩大窗口 [left, right]，直到窗口中的字符串符合要求（包含了 T 中的所有字符）
            ch = s[right]
            if ch in needs:
                window[ch] += 1
                if window[ch] == needs[ch]:
                    match += 1
            right += 1

            while match == len(
                    needs):  # 停止增加 right，转而不断增加 left 指针缩小窗口 [left, right]，直到窗口中的字符串不再符合要求（不包含 T 中的所有字符了）。同时，每次增加 left，我们都要更新一轮结果
                if right - left < size:
                    start = left
                    size = right - left
                ch = s[left]
                if ch in needs:
                    window[ch] -= 1
                    if window[ch] < needs[ch]:
                        match -= 1
                left += 1
        if size == float('inf'):
            return ""
        return s[start:start + size]