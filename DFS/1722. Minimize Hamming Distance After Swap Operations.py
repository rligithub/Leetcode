class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # similar to 1202 SMALLEST STRING WITH SWAPS
        # step1: build graph to connect all swap_index
        graph = collections.defaultdict(list)

        for u, v in allowedSwaps:
            graph[u].append(v)
            graph[v].append(u)

        n = len(source)
        visited = set()
        # step2: for loop each index, to find number of common elements between source and target
        count = 0
        for i in range(n):
            if i in visited:
                continue
            swap_index = []
            self.dfs(graph, i, visited, swap_index)

            # count1 = collections.Counter(source[j] for j in swap_index)
            # count2 = collections.Counter(target[j] for j in swap_index)
            # count += sum((count1 & count2).values()) # how many num in commons
            count1 = collections.defaultdict(int)
            count2 = collections.defaultdict(int)
            for j in swap_index:
                count1[source[j]] += 1  # count1 --> save source 对应位置的num和num的个数
                count2[target[j]] += 1  # count2 --> save target 对应位置的num和num的个数

            for k in count1:
                if k in count2:
                    count += min(count1[k], count2[k])  # find how many common num
        # step3: return numbers of elements not in common
        return n - count

    def dfs(self, graph, i, visited, swap_index):
        visited.add(i)
        swap_index.append(i)
        for nei in graph[i]:
            if nei not in visited:
                self.dfs(graph, nei, visited, swap_index)