class Solution:  # 比较每个word的同index上的char，如果前面相同，比较不同的那位。不同的时候 --> word1[i]:word2[i]
    def alienOrder(self, words: List[str]) -> str:
        # step1: build graph ---> char1 must be pre-requisited of char2

        indegrees = collections.defaultdict(int)
        for word in words:
            for ch in word:
                indegrees[ch] = 0

        order = collections.defaultdict(set)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            find_diff = False
            for j in range(min(len(w1), len(w2))):
                ch1, ch2 = w1[j], w2[j]
                if ch1 != ch2:
                    if ch2 not in order[ch1]:  # de-duplicated
                        indegrees[ch2] += 1
                    order[ch1].add(ch2)
                    find_diff = True
                    break
            if find_diff == False and len(w1) > len(w2):  # ab vs a --> invalid
                return ''

        print(order)
        # step2: BFS
        queue = collections.deque()
        for ch in indegrees.keys():
            if indegrees[ch] == 0:
                queue.append(ch)

        path = ''
        while queue:
            cur = queue.popleft()
            path += cur
            for nei in order[cur]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)

        if len(path) == len(indegrees):
            return path
        return ''
