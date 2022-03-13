class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        n = len(pattern)
        hashmap = {}
        return self.dfs(pattern, s, 0, hashmap)

    def dfs(self, pattern, s, pos, hashmap):

        if pos >= len(pattern) and not s:
            return True

        if pos >= len(pattern) and s:
            return False

        for i in range(1, len(s) + 1):
            if pattern[pos] in hashmap and hashmap[pattern[pos]] == s[:i]:
                if self.dfs(pattern, s[i:], pos + 1, hashmap):
                    return True
            elif pattern[pos] not in hashmap and s[:i] not in hashmap.values():
                hashmap[pattern[pos]] = s[:i]
                if self.dfs(pattern, s[i:], pos + 1, hashmap):
                    return True
                del hashmap[pattern[pos]]
        return False



