# first solution using lists,
# insert in list is O(n), remove is O(1),
# pushing to stack is O(n) and top and pop from stack are O(n^2)
class MyStack:

    def __init__(self):
        self.mainQueue = []
        self.auxQueue = []

    def push(self, x: int) -> None:
        self.mainQueue.insert(0, x)
        print(self.mainQueue)

    def pop(self) -> int:
        self.auxQueue = []
        initialLen = len(self.mainQueue)
        lastItem = -1
        for i in range(len(self.mainQueue)):
            if i == initialLen - 1:
                lastItem = self.mainQueue.pop()
            else:
                self.auxQueue.insert(0, self.mainQueue.pop())

        self.mainQueue = self.auxQueue
        return lastItem

    def top(self) -> int:
        self.auxQueue = []
        initialLen = len(self.mainQueue)
        lastItem = -1
        for i in range(len(self.mainQueue)):
            if i == initialLen - 1:
                lastItem = self.mainQueue.pop()
                self.auxQueue.insert(0, lastItem)
            else:
                self.auxQueue.insert(0, self.mainQueue.pop())

        self.mainQueue = self.auxQueue
        return lastItem

    def empty(self) -> bool:
        return len(self.mainQueue) == 0


# second solution using a Queue implemented with linked list,
# insert in queue is O(1), pop is O(1)
# pushing to the stack is O(1) and top and pop from stack are O(n)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def push(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.first = newNode
            self.last = newNode

        self.last.next = newNode
        self.last = newNode

        self.length += 1

    def pop(self):
        if self.isEmpty():
            return None

        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next

        self.length -= 1
        return temp.value

    def isEmpty(self):
        return self.length == 0


class MyStack:

    def __init__(self):
        self.mainQueue = Queue()
        self.auxQueue = Queue()

    def push(self, x: int) -> None:
        self.mainQueue.push(x)

    def pop(self) -> int:
        self.auxQueue = Queue()
        initialLen = self.mainQueue.length
        lastItem = -1
        for i in range(initialLen):
            if i == initialLen - 1:
                lastItem = self.mainQueue.pop()
            else:
                self.auxQueue.push(self.mainQueue.pop())

        self.mainQueue = self.auxQueue
        return lastItem

    def top(self) -> int:
        self.auxQueue = Queue()
        initialLen = self.mainQueue.length
        lastItem = -1
        for i in range(initialLen):
            if i == initialLen - 1:
                lastItem = self.mainQueue.pop()
                self.auxQueue.push(lastItem)
            else:
                self.auxQueue.push(self.mainQueue.pop())

        self.mainQueue = self.auxQueue
        return lastItem

    def empty(self) -> bool:
        return self.mainQueue.isEmpty()


# third solution using just one queue, instead of two, time complexities are the same as the second solution
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def push(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.first = newNode
            self.last = newNode

        self.last.next = newNode
        self.last = newNode

        self.length += 1

    def pop(self):
        if self.isEmpty():
            return None

        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next

        self.length -= 1
        return temp.value

    def isEmpty(self):
        return self.length == 0


class MyStack:

    def __init__(self):
        self.mainQueue = Queue()

    def push(self, x: int) -> None:
        self.mainQueue.push(x)

    def pop(self) -> int:
        lastItem = -1
        for i in range(self.mainQueue.length):
            if i == self.mainQueue.length - 1:
                lastItem = self.mainQueue.pop()
            else:
                temp = self.mainQueue.pop()
                self.mainQueue.push(temp)

        return lastItem

    def top(self) -> int:
        lastItem = -1
        for i in range(self.mainQueue.length):
            if i == self.mainQueue.length - 1:
                lastItem = self.mainQueue.pop()
                self.mainQueue.push(lastItem)
            else:
                temp = self.mainQueue.pop()
                self.mainQueue.push(temp)

        return lastItem

    def empty(self) -> bool:
        return self.mainQueue.isEmpty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
