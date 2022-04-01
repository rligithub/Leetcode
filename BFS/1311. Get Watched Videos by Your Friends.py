class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> \
    List[str]:
        # level 1 --> your friend
        # level 2 --> your friend's friend

        # step1: bfs --> find the ppl in the given level
        queue = collections.deque()
        queue.append(id)
        visited = set()
        visited.add(id)

        step = 0
        ppl = []
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()

                if step == level:
                    ppl.append(cur)

                for nei in friends[cur]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            step += 1

            # step2: return the watchedVideos
        hashmap = collections.defaultdict(int)
        for p in ppl:
            for video in watchedVideos[p]:
                hashmap[video] += 1

        res = list(hashmap.keys())
        res.sort(key=lambda x: (hashmap[x], x))
        return res




