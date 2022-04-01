class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # similar to word lader
        bank = set(bank)
        queue = collections.deque()
        queue.append((start, 0))
        visited = set()
        visited.add(start)

        while queue:
            cur, count = queue.popleft()
            if cur == end:
                return count

            for nei in self.findnext(cur, bank):
                if nei not in visited:
                    queue.append((nei, count + 1))
                    visited.add(nei)

        return -1

    def findnext(self, word, bank):

        res = []
        for i, ch in enumerate(word):
            for new_ch in "ACGT":
                if ch == new_ch:
                    continue
                new_word = word[:i] + new_ch + word[i + 1:]
                if new_word in bank:
                    res.append(new_word)
        return res
