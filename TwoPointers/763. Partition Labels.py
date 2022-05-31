class Solution1:
    def partitionLabels(self, s: str) -> List[int]:
        # 先数一遍 所有的 letter 的frequency --> 然后再分，分的时候比较下当前的letter的个数和frequency 是不是一样
        # sliding window --> res.append(size of subarray)

        counter = collections.Counter(s)

        window = collections.defaultdict(int)
        res = []

        left, right = 0, 0
        match = 0
        while right < len(s):
            window[s[right]] += 1
            if window[s[right]] == counter[s[right]]:
                match += 1

            if len(window) == match:
                res.append(right - left + 1)
                window = collections.defaultdict(int)
                match = 0
                left = right + 1

            right += 1
        return res


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 先数一遍 所有的 letter 的frequency --> 然后再分，分的时候比较下当前的letter的个数和frequency 是不是一样

        counter = collections.Counter(s)

        window = collections.defaultdict(int)
        res = []

        left, right = 0, 0
        match = 0
        while right < len(s):
            window[s[right]] += 1
            if window[s[right]] == counter[s[right]]:
                match += 1
            right += 1

            if len(window) == match:
                res.append(right - left)
                window = collections.defaultdict(int)
                match = 0
                left = right

        return res
