class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # 找cycle --> need to find root first
        root = 0  # root 肯定不能作为别人的左右孩子
        childrenNodes = set(leftChild + rightChild)
        for i in range(n):
            if i not in childrenNodes:
                root = i
                break

        visited = set()

        queue = collections.deque()
        queue.append(root)

        while queue:
            cur = queue.popleft()
            if cur in visited:
                return False
            else:
                visited.add(cur)
            if leftChild[cur] != -1:
                queue.append(leftChild[cur])

            if rightChild[cur] != -1:
                queue.append(rightChild[cur])

        if len(visited) == n:
            return True
        else:
            return False

class Solution: # DFS
    def validateBinaryTreeNodes(self, n, left, right):
        visited = collections.defaultdict(int)
        indegree = collections.defaultdict(int)
        visited[-1] = 1

        # Return false if any cycles are detected
        if any(self.has_cycle(visited, indegree, left, right, node) for node in range(n)):
            return False

        # Return true if there is exactly 1 root and all other nodes have exactly 1 parent
        count = 0
        for u in range(n):
            if indegree[u] > 1:
                return False
            if indegree[u] == 0:
                count += 1
        return count == 1

    def has_cycle(self, visited, indegree, left, right, node):
        if visited[node] == 1:
            indegree[node] += 1
            return False
        if visited[node] == -1:
            return True
        visited[node] = -1
        if self.has_cycle(visited, indegree, left, right, left[node]) or self.has_cycle(visited, indegree, left, right,right[node]):
            return True
        visited[node] = 1
        return False