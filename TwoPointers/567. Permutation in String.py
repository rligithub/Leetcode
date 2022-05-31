class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # compare freq of char in both s1 and s2 + sliding window

        counter = collections.Counter(s1)

        window = collections.defaultdict(int)
        left, right = 0, 0
        match = 0

        while right < len(s2):
            ch = s2[right]
            right += 1
            if ch in counter:
                window[ch] += 1
                if window[ch] == counter[ch]:
                    match += 1
            if right - left >= len(s1):
                if match == len(counter):
                    return True
                ch = s2[left]
                left += 1
                if ch in counter:
                    if window[ch] == counter[ch]:  # only match -= 1 once
                        match -= 1
                    window[ch] -= 1
        return False

