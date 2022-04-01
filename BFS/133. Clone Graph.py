class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node

        hashmap = {}
        queue = collections.deque([node])
        hashmap[node] = Node(node.val, [])

        while queue:
            currNode = queue.popleft()

            for nei in currNode.neighbors:
                if nei not in hashmap:
                    hashmap[nei] = Node(nei.val, [])
                    queue.append(nei)
                hashmap[currNode].neighbors.append(hashmap[nei])

        return hashmap[node]
