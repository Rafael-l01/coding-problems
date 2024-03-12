# solution using array
class MinStack:

    def __init__(self):
        self.stack = []
        self.height = 0
        self.min = 2**31

    def push(self, val: int) -> None:
        self.min = val if self.min > val else self.min

        self.stack.append({"value": val, "min": self.min})
        self.height += 1

    def pop(self) -> None:
        self.stack.pop()
        self.height -= 1

        if self.stack:
            self.min = self.stack[-1]["min"]
        else:
            self.min = 2**31

    def top(self) -> int:
        return self.stack[-1]["value"]

    def getMin(self) -> int:
        return self.min


# solution using linked list
class Node:
    def __init__(self, value: int, min: int):
        self.value = value
        self.min = min
        self.next = None


class MinStackLinkedList:

    def __init__(self):
        self.topNode = None
        self.height = 0
        self.min = 2**31

    def push(self, val: int) -> None:
        self.min = val if self.min > val else self.min

        newNode = Node(val, self.min)
        newNode.next = self.topNode
        self.topNode = newNode

        self.height += 1

    def pop(self) -> None:
        temp = self.topNode
        self.topNode = self.topNode.next
        temp.next = None

        self.height -= 1

        if self.topNode:
            self.min = self.topNode.min
        else:
            self.min = 2**31

    def top(self) -> int:
        return self.topNode.value

    def getMin(self) -> int:
        return self.min
