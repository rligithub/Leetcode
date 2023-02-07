class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        window = collections.defaultdict(int)

        count = 0
        left, right = 0, 0

        while right < len(s):
            ch1 = s[right]
            window[ch1] += 1
            right += 1

            while len(window) > 2:
                ch2 = s[left]
                window[ch2] -= 1
                if window[ch2] == 0:
                    del window[ch2]
                left += 1
            count = max(count, right - left)

        return count


def generate_substr(s, k):
    if not s or k == 0:
        return None

    result = {}

    for i in range(len(s)):
        if len(s) - i < k:
            break
        if len(set(s[i:i + k])) == k:
            result[s[i:i + k]] = 1
    return result.keys()