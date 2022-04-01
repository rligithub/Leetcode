class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        queue = deque(nestedList)

        depth = 1
        total = 0

        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.pop()
                if cur.isInteger():
                    total += cur.getInteger() * depth
                else:
                    queue.extendleft(cur.getList())
            depth += 1

        return total