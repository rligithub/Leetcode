class Solution:
    def generatePalindromes(self, s: str) -> List[str]:

        count = collections.defaultdict(int)
        for ch in s:
            count[ch] += 1

        odds = 0
        self.odd_char = ""
        for k, v in count.items():
            if v % 2 == 1:
                odds += 1
                self.odd_char = k

            if odds > 1:
                return []
        res = []
        self.dfs(s, count, '', res)

        return res

    def dfs(self, s, count, path, res):

        if len(path) == len(s) // 2:
            res.append(path + self.odd_char + path[::-1])
            return res

        for ch, v in count.items():
            if v >= 2:
                count[ch] -= 2
                self.dfs(s, count, path + ch, res)
                count[ch] += 2


class Solution2:  # TLE
    def generatePalindromes(self, s: str) -> List[str]:
        # permuation + palindrome

        res = []

        s = list(s)
        self.dfs(s, 0, res)
        return res

    def dfs(self, s, pos, res):

        if pos == len(s) and self.isPalindrome(s[:]):
            res.append("".join(s))
            return

        visited = set()
        for i in range(pos, len(s)):
            if s[i] in visited:  # deduplicated
                continue
            visited.add(s[i])

            s[pos], s[i] = s[i], s[pos]
            self.dfs(s, pos + 1, res)
            s[pos], s[i] = s[i], s[pos]

    def isPalindrome(self, s):
        i, j = 0, len(s) - 1

        while i <= j and s[i] == s[j]:
            i += 1
            j -= 1
        return i > j

