class ListNode:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = {}  # hashmap

        self.head = ListNode(0, 0)  # double linkedList
        self.tail = ListNode(0, 0)
        self.head.prev = None
        self.head.next = self.tail

        self.tail.prev = self.head
        self.tail.next = None

    def get(self, key: int) -> int:
        if key in self.table:  # check if it's in hashmap --> {key: ListNode} --> ListNode(key, val) --> return val
            curNode = self.table[key]
            self.removeNode(curNode)
            self.addLastNode(curNode)
            return curNode.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            curNode = self.table[key]
            self.removeNode(curNode)

        newNode = ListNode(key, value)
        self.addLastNode(newNode)  # add in linkedlist
        self.table[key] = newNode  # add in hashmap

        if len(self.table) > self.capacity:  # check if it's oversized --> delete first node
            firstNode = self.head.next
            self.removeNode(firstNode)  # delete from linkedlist
            del self.table[firstNode.key]  # delete from hashmap

    def removeNode(self, node):  # linkedlist: make p points to n, make n points back to p
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def addLastNode(self, node):  # likedlist: add node at last
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)