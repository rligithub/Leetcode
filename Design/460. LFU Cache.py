class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.prev, self.head.next = None, self.tail
        self.tail.prev, self.tail.next = self.head, None
        self.size = 0

    def addLastNode(self, node):
        n = self.tail.prev
        n.next = node
        self.tail.prev = node
        node.prev, node.next = n, self.tail

        self.size += 1

    def removeNode(self, node=None):
        if not node:
            node = self.head.next

        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

        self.size -= 1
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 0
        self.table = {}
        self.freqTable = collections.defaultdict(DLL)

    def get(self, key: int) -> int:
        if key in self.table:
            curNode = self.table[key]
            self.updateFreq(curNode)  # 调整freq
            return curNode.val
        return -1

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return

        if key in self.table:
            curNode = self.table[key]
            self.updateFreq(curNode)
            curNode.val = value
        else:
            if len(self.table) == self.capacity:
                removedNode = self.freqTable[self.minFreq].removeNode()
                del self.table[removedNode.key]

            newNode = ListNode(key, value)
            self.freqTable[1].addLastNode(newNode)
            self.table[key] = newNode
            self.minFreq = 1

    def updateFreq(self, node):
        curFreq = node.freq
        node.freq += 1
        self.freqTable[curFreq].removeNode(node)  # 把旧的freq去掉，删去第一个
        self.freqTable[node.freq].addLastNode(node)  # 把新的freq加上，加在最后
        if curFreq == self.minFreq and self.freqTable[curFreq].size == 0:  # 更新新的minfreq的值
            self.minFreq += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)