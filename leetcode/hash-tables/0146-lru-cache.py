class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.hashMap = {}
        self.capacity = capacity
        self.lru = Node(0, 0)
        self.mru = Node(0, 0)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def insertNodeInList(self, node):
        lastNode = self.mru.prev
        lastNode.next = node
        self.mru.prev = node

        node.prev = lastNode
        node.next = self.mru

    def removeNodeFromList(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key: int) -> int:
        if key in self.hashMap:
            node = self.hashMap[key]
            self.removeNodeFromList(node)
            self.insertNodeInList(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            oldNode = self.hashMap[key]
            self.removeNodeFromList(oldNode)

        newNode = Node(key, value)
        self.insertNodeInList(newNode)
        self.hashMap[key] = newNode

        if len(self.hashMap) > self.capacity:
            lruNode = self.lru.next
            self.removeNodeFromList(lruNode)
            del self.hashMap[lruNode.key]
